# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard3.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)
import ressources.icons.ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1263, 761)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-radius:10px")
        self.verticalLayout_11 = QVBoxLayout(self.main_menu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 3, 7, 0)
        self.widget_8 = QWidget(self.main_menu)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_10 = QVBoxLayout(self.widget_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"QWidget{\n"
"background-color:rgb(236, 236, 236);\n"
"radius:10px;}\n"
"QLineEdit{\n"
"radius:0px;\n"
"background-color: white;\n"
"border:2px solid white;\n"
"border-bottom-color: rgb(65,105,225);\n"
"color:rgbd(0,0,0,0);\n"
"width:40px;\n"
"padding-bottom:7px;\n"
"}\n"
"QLineEdit: hover{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color: white;\n"
"\n"
"}\n"
"QLineEdit: focus{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color:rgb(236, 236, 236);\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menu_btn_2 = QPushButton(self.widget_10)
        self.menu_btn_2.setObjectName(u"menu_btn_2")
        icon = QIcon()
        icon.addFile(u":/icon/menu-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icon/menu-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.menu_btn_2.setIcon(icon)
        self.menu_btn_2.setIconSize(QSize(40, 40))
        self.menu_btn_2.setCheckable(True)
        self.menu_btn_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.menu_btn_2)

        self.horizontalSpacer_3 = QSpacerItem(287, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.search_input = QLineEdit(self.widget_10)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.search_input)

        self.search_btn_2 = QPushButton(self.widget_10)
        self.search_btn_2.setObjectName(u"search_btn_2")
        icon1 = QIcon()
        icon1.addFile(u":/icon/search-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn_2.setIcon(icon1)
        self.search_btn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.search_btn_2)

        self.horizontalSpacer_4 = QSpacerItem(287, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.widget_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icon/notification-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.user = QPushButton(self.widget_10)
        self.user.setObjectName(u"user")
        icon3 = QIcon()
        icon3.addFile(u":/icon/user-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user.setIcon(icon3)
        self.user.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.user)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.stackedWidget_2 = QStackedWidget(self.widget_8)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"radius:10px;\n"
"background-color:rgb(236, 236, 236);\n"
"")
        self.stackedWidget_2.setFrameShadow(QFrame.Sunken)
        self.dash_page = QWidget()
        self.dash_page.setObjectName(u"dash_page")
        self.label_5 = QLabel(self.dash_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 260, 55, 16))
        self.stackedWidget_2.addWidget(self.dash_page)
        self.books_page = QWidget()
        self.books_page.setObjectName(u"books_page")
        self.books_page.setStyleSheet(u"/* ==========================\n"
"   \ud83d\udcda TableView (Livres)\n"
"   ========================== */\n"
"\n"
"QTableView {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #DDDDDD;\n"
"    gridline-color: #BBBBBB;\n"
"    selection-background-color: rgba(5, 19, 128, 0.2);\n"
"    selection-color: #051380;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* \ud83d\udccc Ent\u00eate de la Table */\n"
"QHeaderView::section {\n"
"    background-color: rgb(5, 19, 128);\n"
"    color: white;\n"
"    padding: 8px;\n"
"    border: 1px solid #DDDDDD;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \ud83d\udee0\ufe0f Alternance des couleurs de lignes */\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: rgba(5, 19, 128, 0.2);\n"
"    color: #051380;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \ud83c\udfa8 Effet Hover */\n"
"QTableView::item:hover {\n"
"    background-color: rgba(5, 19, 128, 0.1);\n"
""
                        "}\n"
"")
        self.tableView_books = QTableView(self.books_page)
        self.tableView_books.setObjectName(u"tableView_books")
        self.tableView_books.setGeometry(QRect(10, 250, 961, 401))
        self.stackedWidget_2.addWidget(self.books_page)
        self.authors_page = QWidget()
        self.authors_page.setObjectName(u"authors_page")
        self.verticalLayout_9 = QVBoxLayout(self.authors_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_2 = QWidget(self.authors_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color:rgb(236, 236, 236);\n"
"radius:10px;}\n"
"QLineEdit{\n"
"radius:0px;\n"
"background-color: white;\n"
"border:2px solid white;\n"
"border-bottom-color: rgb(65,105,225);\n"
"color:rgbd(0,0,0,0);\n"
"width:40px;\n"
"padding-bottom:7px;\n"
"}\n"
"QLineEdit: hover{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color: white;\n"
"\n"
"}\n"
"QLineEdit: focus{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color:rgb(236, 236, 236);\n"
"\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_7.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_7.addWidget(self.lineEdit_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.horizontalSpacer_2 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.widget_3 = QWidget(self.authors_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget{\n"
"background-color:rgb(236, 236, 236);\n"
"radius:10px;}\n"
"QLineEdit{\n"
"radius:0px;\n"
"background-color: white;\n"
"border:2px solid white;\n"
"border-bottom-color: rgb(65,105,225);\n"
"color:rgbd(0,0,0,0);\n"
"width:40px;\n"
"padding-bottom:7px;\n"
"}\n"
"QLineEdit: hover{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color: white;\n"
"\n"
"}\n"
"QLineEdit: focus{\n"
"border-bottom-color:2px solid rgb(74,144,226);\n"
"background-color:rgb(236, 236, 236);\n"
"\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_8.addWidget(self.lineEdit_4)

        self.dateEdit = QDateEdit(self.widget_3)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_8.addWidget(self.dateEdit)

        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_8.addWidget(self.lineEdit_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout_9.addWidget(self.widget_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.authors_page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(0, 0, 127)\n"
"	color:white;\n"
"	text-align:left;\n"
"	padding-left:10px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:rgb(255, 255, 255);\n"
"	color:rgb(5, 19, 128);\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"	height:60px;\n"
"	color:rgb(5, 19, 128);\n"
"	font-weight:bold;\n"
"}	")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon5 = QIcon()
        icon5.addFile(u":/icon/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon6 = QIcon()
        icon6.addFile(u":/icon/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(808, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.widget)

        self.tableView_authors = QTableView(self.authors_page)
        self.tableView_authors.setObjectName(u"tableView_authors")
        self.tableView_authors.setStyleSheet(u"/* ==========================\n"
"   \ud83d\udcda TableView (Livres)\n"
"   ========================== */\n"
"\n"
"QTableView {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #DDDDDD;\n"
"    gridline-color: #BBBBBB;\n"
"    selection-background-color: rgba(5, 19, 128, 0.2);\n"
"    selection-color: #051380;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* \ud83d\udccc Ent\u00eate de la Table */\n"
"QHeaderView::section {\n"
"    background-color: rgb(5, 19, 128);\n"
"    color: white;\n"
"    padding: 8px;\n"
"    border: 1px solid #DDDDDD;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \ud83d\udee0\ufe0f Alternance des couleurs de lignes */\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: rgba(5, 19, 128, 0.2);\n"
"    color: #051380;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \ud83c\udfa8 Effet Hover */\n"
"QTableView::item:hover {\n"
"    background-color: rgba(5, 19, 128, 0.1);\n"
""
                        "}\n"
"")

        self.verticalLayout_5.addWidget(self.tableView_authors)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.stackedWidget_2.addWidget(self.authors_page)
        self.loans_page = QWidget()
        self.loans_page.setObjectName(u"loans_page")
        self.label_8 = QLabel(self.loans_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 280, 55, 16))
        self.stackedWidget_2.addWidget(self.loans_page)
        self.sub_page = QWidget()
        self.sub_page.setObjectName(u"sub_page")
        self.label_9 = QLabel(self.sub_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(500, 270, 55, 21))
        self.stackedWidget_2.addWidget(self.sub_page)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


        self.verticalLayout_11.addWidget(self.widget_8)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(5, 19, 128);\n"
"	border-top-right-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	padding-left:3px;\n"
"	border-radius:10px;\n"
"	height:40px;\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:rgb(255, 255, 255);\n"
"	color:rgb(5, 19, 128);\n"
"	border-radius:10px;\n"
"	color:rgb(5, 19, 128);\n"
"	font-weight:bold;\n"
"	\n"
"}	")
        self.verticalLayout_6 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 15, -1, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.uit_logo = QLabel(self.icon_only_widget)
        self.uit_logo.setObjectName(u"uit_logo")
        self.uit_logo.setMinimumSize(QSize(60, 60))
        self.uit_logo.setMaximumSize(QSize(60, 60))
        self.uit_logo.setStyleSheet(u"")
        self.uit_logo.setPixmap(QPixmap(u":/icon/uit-white.png"))
        self.uit_logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.uit_logo)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 0, 6, -1)
        self.dashboars_btn = QPushButton(self.icon_only_widget)
        self.dashboars_btn.setObjectName(u"dashboars_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon/dashboard-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icon/dashboard-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboars_btn.setIcon(icon7)
        self.dashboars_btn.setIconSize(QSize(30, 30))
        self.dashboars_btn.setCheckable(True)
        self.dashboars_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboars_btn)

        self.books_btn = QPushButton(self.icon_only_widget)
        self.books_btn.setObjectName(u"books_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icon/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icon/books-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.books_btn.setIcon(icon8)
        self.books_btn.setIconSize(QSize(30, 30))
        self.books_btn.setCheckable(True)
        self.books_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.books_btn)

        self.author_btn = QPushButton(self.icon_only_widget)
        self.author_btn.setObjectName(u"author_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icon/loan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icon/loan-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.author_btn.setIcon(icon9)
        self.author_btn.setIconSize(QSize(30, 30))
        self.author_btn.setCheckable(True)
        self.author_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.author_btn)

        self.loans_btn = QPushButton(self.icon_only_widget)
        self.loans_btn.setObjectName(u"loans_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icon/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icon/clock-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.loans_btn.setIcon(icon10)
        self.loans_btn.setIconSize(QSize(30, 30))
        self.loans_btn.setCheckable(True)
        self.loans_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.loans_btn)

        self.subscribers_btn = QPushButton(self.icon_only_widget)
        self.subscribers_btn.setObjectName(u"subscribers_btn")
        icon11 = QIcon()
        icon11.addFile(u":/icon/sub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icon/sub-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.subscribers_btn.setIcon(icon11)
        self.subscribers_btn.setIconSize(QSize(30, 30))
        self.subscribers_btn.setCheckable(True)
        self.subscribers_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.subscribers_btn)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_32 = QSpacerItem(20, 337, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_32)

        self.exit_btn = QPushButton(self.icon_only_widget)
        self.exit_btn.setObjectName(u"exit_btn")
        icon12 = QIcon()
        icon12.addFile(u":/icon/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icon/exit-dark.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.exit_btn.setIcon(icon12)
        self.exit_btn.setIconSize(QSize(30, 30))
        self.exit_btn.setCheckable(True)
        self.exit_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.exit_btn)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(5, 19, 128);\n"
"	border-top-right-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	padding-left:10px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:rgb(255, 255, 255);\n"
"	color:rgb(5, 19, 128);\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"	height:60px;\n"
"	color:rgb(5, 19, 128);\n"
"	font-weight:bold;\n"
"}	")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 7, 0, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.uit_logo_7 = QLabel(self.icon_name_widget)
        self.uit_logo_7.setObjectName(u"uit_logo_7")
        self.uit_logo_7.setMinimumSize(QSize(50, 50))
        self.uit_logo_7.setMaximumSize(QSize(80, 70))
        self.uit_logo_7.setStyleSheet(u"")
        self.uit_logo_7.setPixmap(QPixmap(u":/icon/uit-white.png"))
        self.uit_logo_7.setScaledContents(True)

        self.horizontalLayout.addWidget(self.uit_logo_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.icon_name_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 90))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(90, 90))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 9, 11, 9)
        self.dashboars_btn_7 = QPushButton(self.icon_name_widget)
        self.dashboars_btn_7.setObjectName(u"dashboars_btn_7")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.dashboars_btn_7.setFont(font1)
        self.dashboars_btn_7.setStyleSheet(u"")
        self.dashboars_btn_7.setIcon(icon7)
        self.dashboars_btn_7.setIconSize(QSize(30, 30))
        self.dashboars_btn_7.setCheckable(True)
        self.dashboars_btn_7.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.dashboars_btn_7)

        self.books_btn_2 = QPushButton(self.icon_name_widget)
        self.books_btn_2.setObjectName(u"books_btn_2")
        self.books_btn_2.setFont(font1)
        self.books_btn_2.setStyleSheet(u"")
        self.books_btn_2.setIcon(icon8)
        self.books_btn_2.setIconSize(QSize(30, 30))
        self.books_btn_2.setCheckable(True)
        self.books_btn_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.books_btn_2)

        self.author_btn_2 = QPushButton(self.icon_name_widget)
        self.author_btn_2.setObjectName(u"author_btn_2")
        self.author_btn_2.setFont(font1)
        self.author_btn_2.setStyleSheet(u"")
        self.author_btn_2.setIcon(icon9)
        self.author_btn_2.setIconSize(QSize(30, 30))
        self.author_btn_2.setCheckable(True)
        self.author_btn_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.author_btn_2)

        self.loans_btn_2 = QPushButton(self.icon_name_widget)
        self.loans_btn_2.setObjectName(u"loans_btn_2")
        self.loans_btn_2.setFont(font1)
        self.loans_btn_2.setStyleSheet(u"")
        self.loans_btn_2.setIcon(icon10)
        self.loans_btn_2.setIconSize(QSize(30, 30))
        self.loans_btn_2.setCheckable(True)
        self.loans_btn_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.loans_btn_2)

        self.subscribers_btn_2 = QPushButton(self.icon_name_widget)
        self.subscribers_btn_2.setObjectName(u"subscribers_btn_2")
        self.subscribers_btn_2.setFont(font1)
        self.subscribers_btn_2.setStyleSheet(u"")
        self.subscribers_btn_2.setIcon(icon11)
        self.subscribers_btn_2.setIconSize(QSize(30, 30))
        self.subscribers_btn_2.setCheckable(True)
        self.subscribers_btn_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.subscribers_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_31 = QSpacerItem(20, 382, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_31)

        self.exit_btn_7 = QPushButton(self.icon_name_widget)
        self.exit_btn_7.setObjectName(u"exit_btn_7")
        self.exit_btn_7.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.exit_btn_7.setFont(font2)
        self.exit_btn_7.setStyleSheet(u"")
        self.exit_btn_7.setIcon(icon12)
        self.exit_btn_7.setIconSize(QSize(30, 30))
        self.exit_btn_7.setCheckable(True)
        self.exit_btn_7.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exit_btn_7)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_btn_2.toggled.connect(self.icon_only_widget.setHidden)
        self.menu_btn_2.toggled.connect(self.icon_name_widget.setVisible)
        self.exit_btn.toggled.connect(MainWindow.close)
        self.exit_btn_7.toggled.connect(MainWindow.close)

        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn_2.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ..", None))
        self.search_btn_2.setText("")
        self.pushButton_2.setText("")
        self.user.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dashbord", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"loans", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Subscribers", None))
        self.uit_logo.setText("")
        self.dashboars_btn.setText("")
        self.books_btn.setText("")
        self.author_btn.setText("")
        self.loans_btn.setText("")
        self.subscribers_btn.setText("")
        self.exit_btn.setText("")
        self.uit_logo_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"UIT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.dashboars_btn_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.books_btn_2.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.author_btn_2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.loans_btn_2.setText(QCoreApplication.translate("MainWindow", u"Loans", None))
        self.subscribers_btn_2.setText(QCoreApplication.translate("MainWindow", u"Subscribers", None))
        self.exit_btn_7.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
        self.help_btn = QPushButton("Help")
        self.verticalLayout_2.addWidget(self.help_btn)

        # Connecter le bouton
        self.help_btn.clicked.connect(lambda: self.switch_page(5))


