"""
单张图片人脸识别
skk制作
2024年10月18日
"""

import random
import sys

sys.path.insert(0, sys.path[0] + "/../")


import cv2
import os

print(f"当前工作目录: {os.getcwd()}")
import time
import torch
import numpy as np
import pandas as pd

from PySide6.QtCore import QTimer, Qt, QTime
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QPixmap, QImage

from main_window_ui import Ui_MainWindow
from face_recognize import face_detector


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 实时时间定时器
        self.realTimer = QTimer(self)
        self.realTimer.timeout.connect(self.update_time)
        self.realTimer.start(1000)
        self.update_time()
        # 摄像头定时器
        self.cap = None
        self.cameraTimer = QTimer()
        self.cameraTimer.timeout.connect(self.update_frame)
        # 按键与函数关联
        self.pushButton_open.clicked.connect(self.open_camera)
        self.pushButton_close.clicked.connect(self.close_camera)

    def update_time(self):
        """更新实时时间"""
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.label_time.setText(current_time)

    def open_camera(self):
        """打开摄像头"""
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("无法打开摄像头")
                self.cap = None
                return
            self.cameraTimer.start(30)

    def update_frame(self):
        """实时更新摄像头显示"""
        ret, frame = self.cap.read()
        if not ret:
            print("无法接收帧而结束")
            self.timer.stop()
            return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        qt_img = QImage(frame.data, w, h, ch * w, QImage.Format.Format_RGB888)
        self.label_camera.setPixmap(QPixmap.fromImage(qt_img))

    def close_camera(self):
        """关闭摄像头"""
        if self.cap:
            self.cameraTimer.stop()
            self.cap.release()
            self.cap = None
            self.label_camera.clear()

    def draw_boxes_and_names(self, frame, face_list):
        # boxes_frame = np.copy(frame)
        for item in face_list:
            sx1 = int(item[2][0])
            sy1 = int(item[2][1])
            sx2 = int(item[2][2])
            sy2 = int(item[2][3])
            cv2.rectangle(frame, (sx1, sy1), (sx2, sy2), (0, 255, 0), 2)
            if int(item[2][1]) > 10:
                cv2.putText(
                    frame,
                    item[0],
                    (int(sx1), int(sy1 - 6)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1.0,
                    (0, 0, 255),
                )
            else:
                cv2.putText(
                    frame,
                    item[0],
                    (int(sx1), int(sy1 + 15)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1.0,
                    (0, 0, 255),
                )
            # 1.2--将人脸特征库的照片显示出出来---
            img_dir = os.path.join(self.rootFeatureImg, item[0])
            img_path = os.path.join(img_dir, "0.jpg")
            image = cv2.imread(img_path)
            if image is not None:
                self.output.setPixmap(self.np_to_qpixmap(image))
        return frame

    def np_to_qpixmap(self, frame):
        """
        将OpenCV的frame转换为QPixmap并保持宽高比
        将 OpenCV 的 BGR 图像转换为 RGB，因为 Qt 使用的是 RGB 色彩空间。
        """
        # 将BGR格式转换为RGB格式
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(
            frame.data, width, height, bytes_per_line, QImage.Format_RGB888
        )
        q_pixmap = QPixmap.fromImage(q_image)

        # 获取 QLabel 的尺寸
        label_width = self.input.width()
        label_height = self.input.height()

        # 根据宽高比缩放图像，保持比例并适应 QLabel 的大小
        scaled_pixmap = q_pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)

        return scaled_pixmap

    def closeEvent(self, event):
        """在窗口关闭时，释放摄像头资源"""

        cv2.destroyAllWindows()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
