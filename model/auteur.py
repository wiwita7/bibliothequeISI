from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from book_ui import Ui_MainWindow  # Import your UI file
from mongo_db import MongoDB  # Import MongoDB connection class

class BookView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mongo = MongoDB()
        self.load_books()

        # Make columns expand with the window size
        self.ui.tableWidget_book.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_books(self):
        books = self.mongo.get_books()
        self.ui.tableWidget_book.setRowCount(len(books))
        self.ui.tableWidget_book.setColumnCount(len(books[0]) if books else 0)

        for row_idx, book in enumerate(books):
            for col_idx, (key, value) in enumerate(book.items()):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget_book.setItem(row_idx, col_idx, item)

        # Set column headers
        if books:
            self.ui.tableWidget_book.setHorizontalHeaderLabels(books[0].keys())
