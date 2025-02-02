# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(776, 548)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 751, 491))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 381, 411))
        self.label.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-radius:10px")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(19, 25, 331, 441))
        self.label_2.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(70,130,180), stop:1 rgb(5, 19, 128));\n"
"border-radius:10px;")
        self.loginLabel = QLabel(self.widget)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(380, 70, 131, 61))
        font = QFont()
        font.setFamilies([u"Roboto Slab ExtraBold"])
        font.setPointSize(24)
        font.setBold(True)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet(u"color: rgb(0,0,128)")
        self.username = QLineEdit(self.widget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(380, 160, 231, 40))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color: white;\n"
"border:2px solid white;\n"
"border-bottom-color: rgb(65,105,225);\n"
"color:rgbd(0,0,0,0);\n"
"padding-bottom:7px;")
        self.username.setEchoMode(QLineEdit.Normal)
        self.username.setCursorPosition(0)
        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(380, 240, 231, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"background-color:white;\n"
"border:2px solid white;\n"
"border-bottom-color: rgb(65,105,225);\n"
"color:rgbd(0,0,0,0);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setCursorPosition(0)
        self.ForgotPass = QLabel(self.widget)
        self.ForgotPass.setObjectName(u"ForgotPass")
        self.ForgotPass.setGeometry(QRect(380, 410, 151, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.ForgotPass.setFont(font3)
        self.uitLogo = QLabel(self.widget)
        self.uitLogo.setObjectName(u"uitLogo")
        self.uitLogo.setGeometry(QRect(20, 30, 161, 161))
        self.uitLogo.setPixmap(QPixmap(u"../ressources/icons/uit-white.png"))
        self.uitLogo.setScaledContents(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 210, 151, 41))
        font4 = QFont()
        font4.setFamilies([u"Roboto Slab Black"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:rgba(255,255,255);\n"
"")
        self.books1 = QLabel(self.widget)
        self.books1.setObjectName(u"books1")
        self.books1.setGeometry(QRect(10, 340, 121, 141))
        font5 = QFont()
        font5.setFamilies([u"Segoe MDL2 Assets"])
        font5.setPointSize(100)
        self.books1.setFont(font5)
        self.books1.setStyleSheet(u"color:rgba(\n"
"70,130,180);")
        self.books1.setPixmap(QPixmap(u"../ressources/icons/library-80.png"))
        self.books1.setScaledContents(True)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 250, 221, 41))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color:rgba(255,255,255);\n"
"")
        self.books2 = QLabel(self.widget)
        self.books2.setObjectName(u"books2")
        self.books2.setGeometry(QRect(120, 340, 131, 141))
        self.books2.setFont(font5)
        self.books2.setStyleSheet(u"color:rgba(\n"
"70,130,180);")
        self.books2.setPixmap(QPixmap(u"../ressources/icons/library-80.png"))
        self.books2.setScaledContents(True)
        self.books3 = QLabel(self.widget)
        self.books3.setObjectName(u"books3")
        self.books3.setGeometry(QRect(240, 340, 121, 141))
        self.books3.setFont(font5)
        self.books3.setStyleSheet(u"color:rgba(\n"
"70,130,180);")
        self.books3.setPixmap(QPixmap(u"../ressources/icons/library-80.png"))
        self.books3.setScaledContents(True)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 350, 111, 41))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgb(0,0,128);\n"
"color:rgb(255,255,255);\n"
"border-radius:5px\n"
"}\n"
"QPushButton#pushButton:presses{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(255,105,100,225);\n"
"background-position:rgb(85,105,225);\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgb(85,105,255);\n"
"}\n"
"\n"
"")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 350, 111, 41))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgb(0,0,128);\n"
"color:rgb(255,255,255);\n"
"border-radius:5px\n"
"}\n"
"QPushButton#pushButton:presses{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:Blue Ranger;\n"
"background-position:rgb(85,105,225);\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgb(85,105,255);\n"
"}\n"
"\n"
"")
        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(380, 300, 231, 16))
        self.toggle_password = QPushButton(self.widget)
        self.toggle_password.setObjectName(u"toggle_password")
        self.toggle_password.setGeometry(QRect(590, 250, 30, 30))
        self.toggle_password.setStyleSheet(u"background: transparent; border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u"../ressources/icons/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggle_password.setIcon(icon)
        self.toggle_password.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.loginLabel.setText(QCoreApplication.translate("Form", u"Login", None))
        self.ForgotPass.setText(QCoreApplication.translate("Form", u"Forgot password?", None))
        self.uitLogo.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Welcome ", None))
        self.books1.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"to our Library", None))
        self.books2.setText("")
        self.books3.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.error.setText("")
        self.toggle_password.setText("")
    # retranslateUi

