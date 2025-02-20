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
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(965, 581)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(80, 30, 320, 480))
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.output = QLabel(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(560, 30, 320, 480))
        self.output.setScaledContents(True)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMargin(-8)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(470, 60, 61, 451))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 331, 31))
        font = QFont()
        font.setFamilies([u"\u4f18\u8bbe\u6807\u9898\u9ed1"])
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9762\u5411\u5b89\u5168\u7cfb\u7edf\u7684\u9762\u90e8\u8bc6\u522b\u7cfb\u7edf", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5f53\u524d\u955c\u5934\u753b\u9762", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u4eba\u8138\u7279\u5f81\u5e93\u4e2d\u7684\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9762\u5411\u5b89\u5168\u7cfb\u7edf\u7684\u9762\u90e8\u8bc6\u522b\u7cfb\u7edf", None))
    # retranslateUi

