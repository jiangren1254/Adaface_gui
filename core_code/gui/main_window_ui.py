# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(320, 0, 20, 581))
        self.line_1.setFrameShape(QFrame.VLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 40, 301, 31))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"font-size: 22px;\n"
" qproperty-alignment: AlignCenter;")
        self.label_title.setWordWrap(False)
        self.label_bg1 = QLabel(self.centralwidget)
        self.label_bg1.setObjectName(u"label_bg1")
        self.label_bg1.setGeometry(QRect(10, 10, 300, 540))
        self.label_bg1.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(72, 94, 105);\n"
" font-size: 20px; padding: 10px;")
        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 500, 300, 50))
        self.label_version.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 100, 284, 344))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_faceInput = QPushButton(self.verticalLayoutWidget)
        self.pushButton_faceInput.setObjectName(u"pushButton_faceInput")
        self.pushButton_faceInput.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_faceInput)

        self.pushButton_face_recog = QPushButton(self.verticalLayoutWidget)
        self.pushButton_face_recog.setObjectName(u"pushButton_face_recog")
        self.pushButton_face_recog.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_face_recog)

        self.pushButton_database = QPushButton(self.verticalLayoutWidget)
        self.pushButton_database.setObjectName(u"pushButton_database")
        self.pushButton_database.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_database)

        self.pushButton_record = QPushButton(self.verticalLayoutWidget)
        self.pushButton_record.setObjectName(u"pushButton_record")
        self.pushButton_record.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_record)

        self.pushButton_about = QPushButton(self.verticalLayoutWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_about)

        self.pushButton_quit = QPushButton(self.verticalLayoutWidget)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setStyleSheet(u"  background-color:rgb(90, 116, 131);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    min-width: 260px;\n"
"    min-height: 30px;\n"
" qproperty-alignment: AlignCenter;")

        self.verticalLayout.addWidget(self.pushButton_quit)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(510, 10, 171, 41))
        self.label_time.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(0, 255, 0);\n"
" font-size: 16px; padding: 10px;\n"
" qproperty-alignment: AlignCenter;")
        self.label_bg2 = QLabel(self.centralwidget)
        self.label_bg2.setObjectName(u"label_bg2")
        self.label_bg2.setGeometry(QRect(340, 10, 341, 41))
        self.label_bg2.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(0, 255, 0);\n"
" font-size: 20px; padding: 10px;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(830, 200, 118, 23))
        self.progressBar.setValue(88)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(690, 0, 20, 581))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(400, 60, 211, 42))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_open = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMaximumSize(QSize(70, 40))
        self.pushButton_open.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(0, 255, 0);\n"
" font-size: 16px; padding: 10px;")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_close = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMaximumSize(QSize(70, 40))
        self.pushButton_close.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(0, 255, 0);\n"
" font-size: 16px; padding: 10px;")

        self.horizontalLayout.addWidget(self.pushButton_close)

        self.label_camera = QLabel(self.centralwidget)
        self.label_camera.setObjectName(u"label_camera")
        self.label_camera.setGeometry(QRect(360, 110, 301, 221))
        self.label_camera.setStyleSheet(u"border: 2px solid black;")
        self.label_recog_result = QLabel(self.centralwidget)
        self.label_recog_result.setObjectName(u"label_recog_result")
        self.label_recog_result.setGeometry(QRect(390, 380, 191, 151))
        self.label_recog_result.setAutoFillBackground(False)
        self.label_recog_result.setStyleSheet(u"border: 2px solid black;")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(330, 340, 371, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_open_2 = QPushButton(self.centralwidget)
        self.pushButton_open_2.setObjectName(u"pushButton_open_2")
        self.pushButton_open_2.setGeometry(QRect(600, 430, 70, 39))
        self.pushButton_open_2.setMaximumSize(QSize(70, 40))
        self.pushButton_open_2.setStyleSheet(u"background-color: rgb(72, 94, 105);\n"
" color:rgb(0, 255, 0);\n"
" font-size: 16px; padding: 10px;")
        self.label_recog_result_2 = QLabel(self.centralwidget)
        self.label_recog_result_2.setObjectName(u"label_recog_result_2")
        self.label_recog_result_2.setGeometry(QRect(710, 10, 271, 541))
        self.label_recog_result_2.setAutoFillBackground(False)
        self.label_recog_result_2.setStyleSheet(u"border: 2px solid black;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(720, 80, 61, 20))
        self.label.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(820, 80, 141, 21))
        self.label_name.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_name_2 = QLabel(self.centralwidget)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setGeometry(QRect(820, 130, 141, 21))
        self.label_name_2.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(720, 130, 91, 20))
        self.label_2.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(730, 200, 91, 20))
        self.label_3.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(730, 280, 91, 20))
        self.label_4.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_name_3 = QLabel(self.centralwidget)
        self.label_name_3.setObjectName(u"label_name_3")
        self.label_name_3.setGeometry(QRect(830, 280, 141, 21))
        self.label_name_3.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(730, 340, 91, 20))
        self.label_5.setStyleSheet(u"\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 16px;\n"
" qproperty-alignment: AlignCenter;\n"
"border: 1px solid black;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(820, 410, 50, 50))
        self.frame.setMaximumSize(QSize(50, 50))
        self.frame.setStyleSheet(u"background-color: red; border-radius: 25px; border: 2px solid black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_recog_result_2.raise_()
        self.label_bg2.raise_()
        self.label_bg1.raise_()
        self.line_1.raise_()
        self.label_title.raise_()
        self.label_version.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_time.raise_()
        self.progressBar.raise_()
        self.line_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_camera.raise_()
        self.label_recog_result.raise_()
        self.line.raise_()
        self.pushButton_open_2.raise_()
        self.label.raise_()
        self.label_name.raise_()
        self.label_name_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_name_3.raise_()
        self.label_5.raise_()
        self.frame.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9762\u5411\u5b89\u5168\u7cfb\u7edf\u7684\u9762\u90e8\u8bc6\u522b\u7cfb\u7edf", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u9762\u5411\u5b89\u5168\u7cfb\u7edf\u7684\u9762\u90e8\u8bc6\u522b\u7cfb\u7edf", None))
        self.label_bg1.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Ver 1.0.0", None))
        self.pushButton_faceInput.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u5f55\u5165", None))
        self.pushButton_face_recog.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u8bc6\u522b", None))
        self.pushButton_database.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u7ba1\u7406", None))
        self.pushButton_record.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u8bb0\u5f55", None))
        self.pushButton_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"real time", None))
        self.label_bg2.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_camera.setText("")
        self.label_recog_result.setText("")
        self.pushButton_open_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
        self.label_recog_result_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d:", None))
        self.label_name.setText("")
        self.label_name_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u8bc1\u53f7:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165\u65f6\u95f4:", None))
        self.label_name_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6307\u793a\u706f:", None))
    # retranslateUi

