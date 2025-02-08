# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addBook.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)
import ressources.icons.icon

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(526, 588)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(230, 230, 230); /* Light gray background */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color:  rgb(240, 240, 240);\n"
"    border: 2px solid rgb(0, 0, 127);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(0, 102, 204);\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(5, 19, 128);\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 176);\n"
"}\n"
"\n"
"#chooseImageButton {\n"
"    background-color: rgb(70, 130, 180); /* Steel Blue */\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#chooseImageButton:h"
                        "over {\n"
"    background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"#chooseImageButton:pressed {\n"
"    background-color: rgb(0, 0, 176);\n"
"}\n"
"")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 528, 577))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"border-radius:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(491, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.frame_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	border-radius:0px;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(500, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 90); /* Dark blue text */\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.label_10)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 90); /* Dark blue text */\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.title_input = QLineEdit(self.frame_5)
        self.title_input.setObjectName(u"title_input")

        self.verticalLayout_3.addWidget(self.title_input)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.author_input = QLineEdit(self.frame_5)
        self.author_input.setObjectName(u"author_input")

        self.verticalLayout_3.addWidget(self.author_input)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.year_input = QLineEdit(self.frame_5)
        self.year_input.setObjectName(u"year_input")

        self.verticalLayout_3.addWidget(self.year_input)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.category_input = QComboBox(self.frame_5)
        self.category_input.setObjectName(u"category_input")
        self.category_input.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(240,240,240); /* Changed to white */\n"
"    border: 2px solid rgb(0, 0, 127); /* Updated border */\n"
"    border-radius: 5px; /* Updated border-radius */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: black; /* Changed to black */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(0, 102, 204); /* Updated focus border */\n"
"    background-color: rgb(240,240,240); /* Ensure background remains white */\n"
"    /*color: black; /* Ensure text remains black */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    border-left: 1px solid #ccc;\n"
"    background-color: rgb(0,0,127);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: rgb(0, 125, 188);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-col"
                        "or: rgb(240,240,240); /* Background color of the dropdown */\n"
"    color: black; /* Text color of the dropdown items */\n"
"}")

        self.verticalLayout_3.addWidget(self.category_input)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.availability_input = QComboBox(self.frame_5)
        self.availability_input.setObjectName(u"availability_input")
        self.availability_input.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.availability_input.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(240,240,240); /* Changed to white */\n"
"    border: 2px solid rgb(0, 0, 127); /* Updated border */\n"
"    border-radius: 5px; /* Updated border-radius */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: black; /* Changed to black */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(0, 102, 204); /* Updated focus border */\n"
"    background-color: rgb(240,240,240); /* Ensure background remains white */\n"
"    /*color: black; /* Ensure text remains black */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    border-left: 1px solid #ccc;\n"
"    background-color: rgb(0,0,127);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: rgb(0, 125, 188);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-col"
                        "or: rgb(240,240,240); /* Background color of the dropdown */\n"
"    color: black; /* Text color of the dropdown items */\n"
"}")

        self.verticalLayout_3.addWidget(self.availability_input)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.isbn_input = QLineEdit(self.frame_6)
        self.isbn_input.setObjectName(u"isbn_input")

        self.verticalLayout_4.addWidget(self.isbn_input)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.description_input = QTextEdit(self.frame_6)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgb(241, 241, 241);\n"
"    border: 2px solid rgb(0, 0, 127);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid rgb(0, 102, 204);\n"
"    background-color: #ffffff;\n"
"}")

        self.verticalLayout_4.addWidget(self.description_input)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.add_image_btn = QPushButton(self.frame_6)
        self.add_image_btn.setObjectName(u"add_image_btn")
        self.add_image_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.add_image_btn)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.number_of_copies_input = QSpinBox(self.frame_6)
        self.number_of_copies_input.setObjectName(u"number_of_copies_input")
        self.number_of_copies_input.setStyleSheet(u"QSpinBox {\n"
"    background-color: rgb(240,240,240); /* Changed to light grey */\n"
"    border: 2px solid rgb(0, 0, 127); /* Updated border */\n"
"    border-radius: 5px; /* Updated border-radius */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: black; /* Changed to black */\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid rgb(0, 102, 204); /* Updated focus border */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    border-left: 1px solid #ccc;\n"
"    border-bottom: 1px solid #ccc;\n"
"    background-color: rgb(0,0,127);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    background-color: rgb(0, 125, 188);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 16px"
                        ";\n"
"    border-left: 1px solid #ccc;\n"
"    border-top: 1px solid #ccc;\n"
"    background-color: rgb(0,0,127);\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    background-color: rgb(0, 125, 188);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")

        self.verticalLayout_4.addWidget(self.number_of_copies_input)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(100, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(60, 0, 60, 0)
        self.save_btn = QPushButton(self.frame_7)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 45))
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.frame_7)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 45))
        self.cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.cancel_btn)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)
        self.close_btn.toggled.connect(self.close_btn.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.close_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Add Book", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Year", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Availability", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"ISBN", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Decription", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"image", None))
        self.add_image_btn.setText(QCoreApplication.translate("Dialog", u"Choose book image", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"number of copies", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

