import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from pymongo import MongoClient
from views.dashbord5 import Ui_MainWindow

class BookView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect to MongoDB
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["library_db"]  # Replace with your actual database name
        self.collection = self.db["book"]  # Replace with your collection name

        # Setup TableWidget
        self.setup_table()
        self.load_books()

    def setup_table(self):
        """Initialize tableWidget_books with headers."""
        self.ui.tableWidget_books.setColumnCount(6)  # Set number of columns
        self.ui.tableWidget_books.setHorizontalHeaderLabels(["_id", "Title", "Author ID", "Genre", "Published Year", "Available Copies"])
        
        # Make columns stretch when resizing
        self.ui.tableWidget_books.horizontalHeader().setStretchLastSection(True)
        for col in range(6):
            self.ui.tableWidget_books.horizontalHeader().setSectionResizeMode(col, 1)  # Resize all columns dynamically

    def load_books(self):
        """Fetch and display books from MongoDB."""
        self.ui.tableWidget_books.setRowCount(0)  # Clear table before loading new data

        books = self.collection.find({}, {"_id": 1, "title": 1, "author_id": 1, "genre": 1, "published_year": 1, "available_copies": 1})

        for row_idx, book in enumerate(books):
            self.ui.tableWidget_books.insertRow(row_idx)
            row_data = [
                str(book.get("_id", "")),
                book.get("title", ""),
                str(book.get("author_id", "")),
                book.get("genre", ""),
                str(book.get("published_year", "")),
                str(book.get("available_copies", ""))
            ]

            for col_idx, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center align text
                self.ui.tableWidget_books.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookView()
    window.show()
    sys.exit(app.exec())
