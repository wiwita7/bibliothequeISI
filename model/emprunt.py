from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QLineEdit, QHeaderView, QComboBox, QListWidget, QSplitter, QFrame
)
from PyQt6.QtGui import QPixmap
import sys

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library System")
        self.setGeometry(100, 100, 900, 500)
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        
        # Side Menu
        side_menu = QListWidget()
        side_menu.addItem("📚 Book")
        side_menu.addItem("📖 E-Books")
        side_menu.addItem("📩 Send Request")
        
        # Splitter to separate side menu and main content
        splitter = QSplitter()
        splitter.addWidget(side_menu)
        
        # Main Content Layout
        content_layout = QVBoxLayout()
        
        # Search Bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for...")
        search_button = QPushButton("Search")
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # Book Title, Category, Cover, Read, Download
        self.table.setHorizontalHeaderLabels(["Book Title", "Category", "Book Cover", "Read", "Download"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Load Data
        self.load_data()
        
        content_layout.addLayout(search_layout)
        content_layout.addWidget(self.table)
        
        # Add content to splitter
        content_frame = QFrame()
        content_frame.setLayout(content_layout)
        splitter.addWidget(content_frame)
        
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
    
    def load_data(self):
        books = [
            ("Architecture", "Programming", "image.png"),
            ("JavaScript", "Programming", "image.png"),
            ("NLP", "Programming", "image.png"),
        ]
        
        self.table.setRowCount(len(books))
        
        for row, (title, category, cover) in enumerate(books):
            self.table.setItem(row, 0, QTableWidgetItem(title))
            self.table.setItem(row, 1, QTableWidgetItem(category))
            
            # Book Cover
            cover_label = QLabel()
            pixmap = QPixmap(cover)
            cover_label.setPixmap(pixmap.scaled(50, 50))
            self.table.setCellWidget(row, 2, cover_label)
            
            # Read Button
            read_button = QPushButton("View PDF")
            self.table.setCellWidget(row, 3, read_button)
            
            # Download Button
            download_button = QPushButton("Download PDF")
            self.table.setCellWidget(row, 4, download_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())
