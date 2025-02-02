import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QLineEdit
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QVBoxLayout, QHeaderView
from views.auteur_view import AuthorsView  # Import the new AuthorsView
from views.livre_view import BooksView
from views.dashboard3 import Ui_MainWindow
class Dashboard(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Dashboard")
        self.setGeometry(100, 100, 1100, 600)
        self.setupUi(self)
        # Set the search_input field text color to Blue Ranger

        self.icon_name_widget.setHidden(True)
        self.center_window()  # Center the login window

        # Setup Navigation
        self.dashboars_btn.clicked.connect(lambda: self.switch_page(0))
        self.dashboars_btn_7.clicked.connect(lambda: self.switch_page(0))
        self.books_btn.clicked.connect(lambda: self.switch_page(1))
        self.books_btn_2.clicked.connect(lambda: self.switch_page(1))
        self.author_btn.clicked.connect(lambda: self.switch_page(2))
        self.author_btn_2.clicked.connect(lambda: self.switch_page(2))
        self.loans_btn.clicked.connect(lambda: self.switch_page(3))
        self.loans_btn_2.clicked.connect(lambda: self.switch_page(3))
        self.subscribers_btn.clicked.connect(lambda: self.switch_page(4))
        self.subscribers_btn_2.clicked.connect(lambda: self.switch_page(4))
                # Set the window to be frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ✅ Load the Authors Table in Page 2
        self.authors_page = AuthorsView()
        self.stackedWidget_2.insertWidget(2, self.authors_page)
        # ✅ Charger la TableView des Livres dans la page 1
        self.books_page = BooksView()
        self.stackedWidget_2.insertWidget(1, self.books_page)
        #centrer
        from views.help_view import HelpView  # Import de la page d'aide
        self.help_page = HelpView()
        self.stackedWidget_2.insertWidget(5, self.help_page)
        self.menu_btn_2.clicked.connect(self.toggle_menu)

    from PySide6.QtCore import QPropertyAnimation, QSize

    def toggle_menu(self):
        """Rétracte/Agrandit le menu latéral"""
        width = self.icon_name_widget.width()
        new_width = 60 if width > 60 else 200

        animation = QPropertyAnimation(self.icon_name_widget, b"maximumWidth")
        animation.setDuration(300)
        animation.setStartValue(width)
        animation.setEndValue(new_width)
        animation.start()
    
    def switch_page(self, index):
        """Change page in QStackedWidget"""
        self.stackedWidget_2.setCurrentIndex(index)

    def switch_to_dashboardPage(self):
        self.stackedWidget_2.setCurrentIndex(0)
    def switch_to_booksPage(self):
        self.stackedWidget_2.setCurrentIndex(1)
    def switch_to_authorPage(self):
        self.stackedWidget_2.setCurrentIndex(2)
    def switch_to_loansPage(self):
        self.stackedWidget_2.setCurrentIndex(3)
    def switch_to_subscribersPage(self):
        self.stackedWidget_2.setCurrentIndex(4)
    def center_window(self):
        """Centers the window on the screen"""
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
