from views.dashbord5 import Ui_MainWindow, QMainWindow, QApplication
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QSizeGrip, QGraphicsOpacityEffect
import sys
from PySide6.QtCore import QTimer
from views.notification import NotificationWindow
from database.book_database import BookDatabase
from views.addBook import Ui_Dialog  
from pymongo import MongoClient
from ajouter_livre import AddBookWindow  # Importer la nouvelle fenêtre


# Database Connection
class Database:
    def __init__(self, db_name="Library_db"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()

# Dashboard Window
class DashboardWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = BookDatabase()
        
        # Window Configurations
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: rgba(0, 0, 0, 100);")
        self.resize(900, 700)
        
        # Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        # Window Icon
        self.setWindowIcon(QIcon(":/icons/uit-dark.png"))
        self.setWindowTitle("UIT Library")
        QSizeGrip(self.ui.size_grip)
        
        # Button Connections
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.restore_win_btn.clicked.connect(self.restore_or_maximize_window)
        self.ui.menu_btn.clicked.connect(self.slideLeftMenu)
        self.ui.home_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.home_page))
        self.ui.book_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.book_page))
        self.ui.author_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.author_page))
        self.ui.loan_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.management_page))
        self.ui.sub_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.sub_page))
        self.ui.add_book_btn_2.clicked.connect(self.open_add_book_window)
        
        self.load_books()
        self.fadeInAnimation()

        self.show()
    
    def open_add_book_window(self):
        """ Ouvre la fenêtre d'ajout de livre """
        self.add_book_window = AddBookWindow()
        self.add_book_window.book_added.connect(self.load_books)  # Mettre à jour la table après ajout
        self.add_book_window.exec()
            

    from PySide6.QtWidgets import QTableWidgetItem

    def load_books(self):
        """ Charge les livres depuis MongoDB et les affiche dans la TableView """
        self.ui.tableWidget_books.setRowCount(0)  # Effacer toutes les lignes avant de recharger

        books = self.db.get_all_books()  # Récupérer les livres depuis MongoDB

        for row, book in enumerate(books):
            self.ui.tableWidget_books.insertRow(row)

            self.ui.tableWidget_books.setItem(row, 0, QTableWidgetItem(str(book.get("_id", "Unknown"))))
            self.ui.tableWidget_books.setItem(row, 1, QTableWidgetItem(book.get("titre", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 2, QTableWidgetItem(book.get("auteur", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 3, QTableWidgetItem(str(book.get("annee_publication", "Unknown"))))
            self.ui.tableWidget_books.setItem(row, 4, QTableWidgetItem(book.get("categorie", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 5, QTableWidgetItem(str(book.get("disponible", "Unknown"))))
            self.ui.tableWidget_books.setItem(row, 6, QTableWidgetItem(book.get("ISBN", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 7, QTableWidgetItem(book.get("description", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 8, QTableWidgetItem(book.get("couverture", "Unknown")))
            self.ui.tableWidget_books.setItem(row, 9, QTableWidgetItem(str(book.get("nombre_exemplaires", "Unknown"))))

    
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_win_btn.setIcon(QIcon(":/icons/minimize.png"))
        else:
            self.showMaximized()
            self.ui.restore_win_btn.setIcon(QIcon(":/icons/maximize.png"))
    
    def slideLeftMenu(self):
        width = self.ui.side_menu_container.width()
        newWidth = 200 if width == 0 else 0
        self.ui.menu_btn.setIcon(QIcon(":/icons/double-left.png" if newWidth == 200 else ":/icons/align-left.png"))
        self.animation = QPropertyAnimation(self.ui.side_menu_container, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
    
    def fadeInAnimation(self):
        self.effect = QGraphicsOpacityEffect(self.ui.centralwidget)
        self.ui.centralwidget.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(600)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
    
    def changePageWithAnimation(self, page):
        current_index = self.ui.stackedWidget.currentIndex()
        next_index = self.ui.stackedWidget.indexOf(page)
        if current_index == next_index:
            return
        self.page_animation = QPropertyAnimation(self.ui.stackedWidget, b"geometry")
        self.page_animation.setDuration(300)
        self.page_animation.setEasingCurve(QEasingCurve.OutCubic)
        offset = self.ui.stackedWidget.width()
        start_pos = QRect(self.ui.stackedWidget.x() + offset, self.ui.stackedWidget.y(), self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
        end_pos = QRect(self.ui.stackedWidget.x(), self.ui.stackedWidget.y(), self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.stackedWidget.setGeometry(start_pos)
        self.page_animation.setStartValue(start_pos)
        self.page_animation.setEndValue(end_pos)
        self.page_animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())
