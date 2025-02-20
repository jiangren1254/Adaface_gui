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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(965, 581)
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
        self.label_time.setGeometry(QRect(580, 290, 141, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_bg1.raise_()
        self.line_1.raise_()
        self.label_title.raise_()
        self.label_version.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_time.raise_()
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
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

