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
import sqlite3
import pandas as pd

from PySide6.QtCore import QTimer, Qt, QTime
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox,QInputDialog
from PySide6.QtGui import QPixmap, QImage

from main_window_ui import Ui_MainWindow
from face_recognize import face_detector

class FaceDatabase:
    def __init__(self, db_name="face_database.db"):
        """ 初始化数据库连接 """
        self.db_name = db_name
        self.create_table()
    def create_table(self):
        """ 创建 face_data 表（如果不存在） """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS face_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                id_card TEXT UNIQUE NOT NULL,
                image BLOB NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    def insert_data(self, name, id_card, frame):
        """ 插入数据：姓名、身份证号、图像 """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()

        try:
            cursor.execute("INSERT INTO face_data (name, id_card, image) VALUES (?, ?, ?)", 
                           (name, id_card, img_bytes))
            conn.commit()
            print("数据插入成功！")
        except sqlite3.IntegrityError:
            print("该身份证号已存在，插入失败！")

        conn.close()
    def delete_data(self, id_card):
        """ 根据身份证号删除数据 """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM face_data WHERE id_card=?", (id_card,))
        conn.commit()

        if cursor.rowcount > 0:
            print("数据删除成功！")
        else:
            print("该身份证号不存在！")

        conn.close()
    def update_data(self, id_card, new_name=None, new_image=None):
        """ 根据身份证号更新姓名或图像 """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if new_name:
            cursor.execute("UPDATE face_data SET name=? WHERE id_card=?", (new_name, id_card))
        
        if new_image is not None:
            _, img_encoded = cv2.imencode('.jpg', new_image)
            img_bytes = img_encoded.tobytes()
            cursor.execute("UPDATE face_data SET image=? WHERE id_card=?", (img_bytes, id_card))

        conn.commit()

        if cursor.rowcount > 0:
            print("数据更新成功！")
        else:
            print("该身份证号不存在，更新失败！")

        conn.close()
    def get_face_data(self, id_card):
        """ 查询数据：根据身份证号获取姓名和图像 """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT name, image FROM face_data WHERE id_card=?", (id_card,))
        result = cursor.fetchone()
        conn.close()

        if result:
            name, img_bytes = result
            img_array = np.frombuffer(img_bytes, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            return name, img
        else:
            print("未找到该身份证号的记录！")
            return None, None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.db = FaceDatabase()
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
        self.pushButton_faceInput.clicked.connect(self.face_input)
        self.pushButton_about.clicked.connect(self.show_about)
        self.pushButton_quit.clicked.connect(self.close_event)
        self.pushButton_open.clicked.connect(self.open_camera)
        self.pushButton_close.clicked.connect(self.close_camera)
    def face_input(self):
        """人脸录入按钮"""
        if self.cap is None or not self.cap.isOpened():
            QMessageBox.warning(self, "提示", "请先打开摄像头！")
            return
        ret, frame = self.cap.read()
        if not ret:
            QMessageBox.critical(self, "错误", "无法获取摄像头图像！")
            return
        name, ok1 = QInputDialog.getText(self, "人脸录入", "请输入姓名：")
        if not ok1 or not name.strip():
            return  
        id_card, ok2 = QInputDialog.getText(self, "人脸录入", "请输入身份证号：")
        if not ok2 or not id_card.strip():
            return 
        self.db.insert_data(name,id_card,frame)
        QMessageBox.information(self, "成功", f"录入成功！\n姓名：{name}\n身份证号：{id_card}")
    def show_about(self):
        """关于按钮"""
        QMessageBox.about(self,"关于",
            "<h3>软件名称：面向安全系统的面部识别系统</h3>"
            "<p><b>作者团队：</b> XXX团队</p>"
            "<p><b>版本号：</b> v1.0.0</p>"
            "<p><b>鸣谢：</b> 感谢所有支持本项目的朋友！</p>",)
    def close_event(self):
        """退出按钮"""
        reply = QMessageBox.question(self,"退出确认","确定要退出吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No,)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
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
        q_pixmap = QPixmap.fromImage(qt_img)
        label_width = self.label_camera.width()
        label_height = self.label_camera.height()
        scaled_pixmap = q_pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)
        self.label_camera.setPixmap(scaled_pixmap)

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

    def closeEvent(self, event):
        """在窗口关闭时，自动调用，释放资源"""
        cv2.destroyAllWindows()
        event.accept()


if __name__ == "__main__":
    # gui界面
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
