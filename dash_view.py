from views.dashbord5 import Ui_MainWindow, QMainWindow, QApplication
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QTableWidgetItem, QDialog
from PySide6.QtGui import QIcon, QColor, QMouseEvent
from PySide6.QtWidgets import QSizeGrip, QGraphicsOpacityEffect
import sys, os
from PySide6.QtCore import QTimer
from views.notification import NotificationWindow
from database.book_database import BookDatabase
from views.addBook import Ui_Dialog  
from views.modifyBook import Ui_DialogModify
from pymongo import MongoClient
from ajouter_livre import AddBookWindow  # Importer la nouvelle fenêtre
from modifier_livre import ModifyBookWindow
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QComboBox, QTableWidgetItem
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter


# Database Connection
class Database:
    def __init__(self, db_name="Library_db"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()
class BookDatabase:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Library_db"]
        self.books_collection = self.db["books"]

    def get_all_books(self):
        return list(self.books_collection.find())

    def get_book_by_id(self, book_id):
        from bson.objectid import ObjectId
        return self.books_collection.find_one({"_id": ObjectId(book_id)})
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
        self.ui.add_book_btn_2.clicked.connect(self.open_add_book_window)# Connect the add button
        self.ui.modify_book_btn_2.clicked.connect(self.modify_selected_book)  # Connect the modify button
        self.ui.print_btn_2.clicked.connect(self.print_books_to_pdf)  # Connect the print button
        self.ui.pushButton_6.clicked.connect(self.filter_table) #connect search line

        # Connect table row click event
        self.ui.tableWidget_books.cellDoubleClicked.connect(self.edit_book)
        # hide row's numbers
        self.ui.tableWidget_books.verticalHeader().setVisible(False)

        self.load_books()
        self.fadeInAnimation()

        self.show()

    def filter_table(self):
        """ Filter table data based on search_lineEdit input across all columns. """
        search_text = self.ui.search_lineEdit.text().strip().lower()

        for row in range(self.ui.tableWidget_books.rowCount()):
            match = False  # Assume no match initially

            for col in range(self.ui.tableWidget_books.columnCount()):
                item = self.ui.tableWidget_books.item(row, col)
                if item and search_text in item.text().strip().lower():
                    match = True
                    break  # Stop checking other columns if one column matches

            self.ui.tableWidget_books.setRowHidden(row, not match)  # Show/hide row

    def print_books_to_pdf(self):
        """ Imprime la liste des livres dans un fichier PDF et le sauvegarde sur le bureau """
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        pdf_path = os.path.join(desktop, "books_list.pdf")
        
        # Ensure the Desktop directory exists
        if not os.path.exists(desktop):
            os.makedirs(desktop)
        
        print(f"Saving PDF to: {pdf_path}")  # Print the path for verification
        
        try:
            c = canvas.Canvas(pdf_path, pagesize=landscape(letter))
            width, height = landscape(letter)

            # Add title
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, height - 40, "UIT Library's Existing Books")
            y = height - 60

            # Set font for table content
            c.setFont("Helvetica", 12)
            
            # Column headers
            c.drawString(50, y, "ID")
            c.drawString(150, y, "Titre")
            c.drawString(300, y, "Auteur")
            c.drawString(450, y, "ISBN")
            c.drawString(550, y, "Catégorie")
            c.drawString(700, y, "Disponibilité")
            c.drawString(850, y, "Description")
            y -= 20

            books = self.db.get_all_books()
            for book in books:
                c.drawString(50, y, f"{book.get('_id', 'Unknown')}")
                c.drawString(150, y, f"{book.get('titre', 'Unknown')}")
                c.drawString(300, y, f"{book.get('auteur', 'Unknown')}")
                c.drawString(450, y, f"{book.get('ISBN', 'Unknown')}")
                c.drawString(550, y, f"{book.get('categorie', 'Unknown')}")
                c.drawString(700, y, f"{book.get('disponible', 'Unknown')}")
                c.drawString(850, y, f"{book.get('description', 'Unknown')}")
                y -= 20
                if y < 40:
                    c.showPage()
                    y = height - 40

            c.save()
            QMessageBox.information(self, "PDF Saved", f"The list of books has been saved to {pdf_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save PDF: {e}")

        ### 🟢 IMPLEMENT DRAGGING FUNCTIONALITY
    def mousePressEvent(self, event: QMouseEvent):
        """ Capture the initial position when the mouse is pressed """
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        """ Move the window when dragging """
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """ Stop dragging when mouse is released """
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def delete_row_from_database(self, book_id):
        # Assuming you have a database connection set up
        connection = self.database_connection
        cursor = connection.cursor()

        # Execute the SQL query to delete the row
        query = "DELETE FROM books WHERE id = ?"
        cursor.execute(query, (book_id,))

        # Commit the changes
        connection.commit()
    def open_add_book_window(self):
        """ Ouvre la fenêtre d'ajout de livre """
        self.add_book_window = AddBookWindow()
        self.add_book_window.book_added.connect(self.load_books)  # Mettre à jour la table après ajout
        self.add_book_window.exec()
    
    def modify_selected_book(self):
        """ Ouvre la fenêtre d'ajout de livre avec les informations de la ligne sélectionnée """
        selected_row = self.ui.tableWidget_books.currentRow()
        if selected_row >= 0:
            book_id = self.ui.tableWidget_books.item(selected_row, 0).text()
            book = self.db.get_book_by_id(book_id)
            
            if book:
                self.add_book_window = ModifyBookWindow()
                self.add_book_window.populate_fields(book)
                self.add_book_window.book_added.connect(self.load_books)  # Mettre à jour la table après modification
                self.add_book_window.exec()
        else:
            QMessageBox.warning(self, "No Selection", "Please select a book to modify.")

    def edit_book(self, row, column):
        """ Ouvre la fenêtre d'ajout de livre avec les informations existantes """
        book_id = self.ui.tableWidget_books.item(row, 0).text()
        book = self.db.get_book_by_id(book_id)
        
        if book:
            self.add_book_window = AddBookWindow()
            self.add_book_window.populate_fields(book)
            self.add_book_window.book_added.connect(self.load_books)  # Mettre à jour la table après modification
            self.add_book_window.exec()

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