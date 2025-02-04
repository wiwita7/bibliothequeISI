# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashbord5.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ressources.icons.icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"*{\n"
"border:none;\n"
"background-color:rgb(0, 0, 127);\n"
"	color:#FFF;\n"
"radius:10px;\n"
"}\n"
"#centralwidget{\n"
"	background-color:#040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color:rgb(0, 0, 127);\n"
"	border-radius:20px;\n"
"	border-buttom:3px solide ;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton{\n"
"	padding:10px;\n"
"	background-color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMinimumSize(QSize(0, 0))
        self.side_menu_container.setMaximumSize(QSize(0, 16777215))
        self.side_menu_container.setSizeIncrement(QSize(2, 0))
        self.side_menu_container.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.side_menu_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.side_menu_container)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(198, 0))
        self.side_menu.setStyleSheet(u"border-left-radius:10px;\n"
"background-color:rgb(5, 19, 128);")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.side_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.side_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(16, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/icons/uit-white.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.side_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setStyleSheet(u"QPushButton:hover{\n"
"/*border-right: 4px solid #C7C223;*/\n"
"border-left: 4px solid #C7C223;\n"
"background-color: #255B98;\n"
"border-radius:0px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"text-align: left;\n"
"\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame_10)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setFont(font)
        self.home_btn.setLayoutDirection(Qt.LeftToRight)
        self.home_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(3530, 30))

        self.verticalLayout_8.addWidget(self.home_btn)

        self.book_btn = QPushButton(self.frame_10)
        self.book_btn.setObjectName(u"book_btn")
        self.book_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.book_btn.setIcon(icon1)
        self.book_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.book_btn)

        self.author_btn = QPushButton(self.frame_10)
        self.author_btn.setObjectName(u"author_btn")
        self.author_btn.setMinimumSize(QSize(60, 20))
        self.author_btn.setFont(font)
        self.author_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.author_btn.setIcon(icon2)
        self.author_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.author_btn)

        self.loan_btn = QPushButton(self.frame_10)
        self.loan_btn.setObjectName(u"loan_btn")
        self.loan_btn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loan_btn.setIcon(icon3)
        self.loan_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.loan_btn)

        self.sub_btn = QPushButton(self.frame_10)
        self.sub_btn.setObjectName(u"sub_btn")
        self.sub_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/sub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sub_btn.setIcon(icon4)
        self.sub_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.sub_btn)


        self.verticalLayout_6.addWidget(self.frame_10, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.side_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.exit_btn = QPushButton(self.frame_9)
        self.exit_btn.setObjectName(u"exit_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.exit_btn)


        self.verticalLayout_4.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.side_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.main_body)
        self.header.setObjectName(u"header")
        self.header.setEnabled(True)
        self.header.setStyleSheet(u"border-top-radius: 10px;\n"
"\n"
"background-color: rgb(5, 19, 128);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(0, 0, 176);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/align-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.menu_btn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 40))
        self.lineEdit.setStyleSheet(u"    QLineEdit {\n"
"        background-color: #f0f0f0; /* Light grey background */\n"
"        border: 2px solid rgb(5, 19, 128); /* Your specified color for the border */\n"
"        border-radius: 5px; /* Rounded corners */\n"
"        padding: 5px; /* Padding inside the text field */\n"
"        color: #333333; /* Dark grey text color */\n"
"        font-size: 14px; /* Font size */\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        border: 2px solid rgb(0, 102, 204); /* Complementary blue color for the border when focused */\n"
"        background-color: #ffffff; /* White background when focused */\n"
"	       box-shadow: 2px 2px 10px rgba(0, 102, 204, 0.5); /* Stronger shadow when focused */\n"
"\n"
"    }\n"
"")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon7 = QIcon()
        icon7.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.users_btn = QPushButton(self.frame_2)
        self.users_btn.setObjectName(u"users_btn")
        self.users_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(0, 0, 176);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.users_btn.setIcon(icon8)
        self.users_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.users_btn)

        self.notification_btn = QPushButton(self.frame_2)
        self.notification_btn.setObjectName(u"notification_btn")
        self.notification_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(0, 0, 176);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/notification.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notification_btn.setIcon(icon9)
        self.notification_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.notification_btn)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignTop)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame_3)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(0, 0, 176);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/down-left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon10)
        self.minimize_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.minimize_btn)

        self.restore_win_btn = QPushButton(self.frame_3)
        self.restore_win_btn.setObjectName(u"restore_win_btn")
        self.restore_win_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 166);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(0, 0, 176);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_win_btn.setIcon(icon11)
        self.restore_win_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.restore_win_btn)

        self.close_btn = QPushButton(self.frame_3)
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
"	border-top-right-radius: 10px;\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon12)
        self.close_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main_bode_contents = QFrame(self.main_body)
        self.main_bode_contents.setObjectName(u"main_bode_contents")
        sizePolicy.setHeightForWidth(self.main_bode_contents.sizePolicy().hasHeightForWidth())
        self.main_bode_contents.setSizePolicy(sizePolicy)
        self.main_bode_contents.setMinimumSize(QSize(200, 0))
        self.main_bode_contents.setStyleSheet(u"background-color:rgb(240, 240, 240);")
        self.main_bode_contents.setFrameShape(QFrame.StyledPanel)
        self.main_bode_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.main_bode_contents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.main_bode_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 190, 331, 161))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.home_page)
        self.book_page = QWidget()
        self.book_page.setObjectName(u"book_page")
        self.label_6 = QLabel(self.book_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(590, 220, 55, 91))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.book_page)
        self.author_page = QWidget()
        self.author_page.setObjectName(u"author_page")
        self.label_7 = QLabel(self.author_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 200, 161, 181))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.author_page)
        self.sub_page = QWidget()
        self.sub_page.setObjectName(u"sub_page")
        self.label_8 = QLabel(self.sub_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(540, 200, 151, 181))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.sub_page)
        self.management_page = QWidget()
        self.management_page.setObjectName(u"management_page")
        self.label_9 = QLabel(self.management_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 210, 55, 191))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.management_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_bode_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border-bottom-radius: 10px;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 0, 0, 6)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 127);")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon13 = QIcon()
        icon13.addFile(u":/icons/ibn-tofail-logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon13)
        self.pushButton_7.setIconSize(QSize(70, 30))

        self.verticalLayout_2.addWidget(self.pushButton_7, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UIT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.book_btn.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.author_btn.setText(QCoreApplication.translate("MainWindow", u"Authors", None))
        self.loan_btn.setText(QCoreApplication.translate("MainWindow", u"Loans", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"Subscribers", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        self.pushButton_6.setText("")
        self.users_btn.setText("")
        self.notification_btn.setText("")
        self.minimize_btn.setText("")
        self.restore_win_btn.setText("")
        self.close_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UIT Library", None))
        self.pushButton_7.setText("")
    # retranslateUi

