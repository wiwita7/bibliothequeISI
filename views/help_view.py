from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QLineEdit, QHeaderView, QComboBox, QListWidget, QSplitter, QFrame
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QPropertyAnimation, QSize
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
        self.side_menu = QListWidget()
        self.side_menu.addItem("📚 Book")
        self.side_menu.addItem("📖 E-Books")
        self.side_menu.addItem("📩 Send Request")
        self.side_menu.setMaximumWidth(200)  # Default expanded width
        
        # Toggle Button
        self.toggle_button = QPushButton("≡")
        self.toggle_button.clicked.connect(self.toggle_menu)
        
        # Sidebar Layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.toggle_button)
        sidebar_layout.addWidget(self.side_menu)
        sidebar_layout.addStretch()
        
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setLayout(sidebar_layout)
        
        # Splitter to separate side menu and main content
        self.splitter = QSplitter()
        self.splitter.addWidget(self.sidebar_frame)
        
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
        self.table.setStyleSheet(""
            "QHeaderView::section {"
            "background-color: #2C3E50;"
            "color: #ECF0F1;"
            "font-size: 18px;"
            "font-weight: bold;"
            "padding: 8px;"
            "border: 1px solid #34495E;"
            "border-radius: 5px;"
            "}"
            "QTableWidget::item {"
            "padding: 12px;"
            "border-bottom: 1px solid #d3d3d3;"
            "}"
            "QTableWidget {"
            "background-color: #F7F9FC;"
            "gridline-color: #D3D3D3;"
            "alternate-background-color: #ECF0F1;"
            "border: none;"
            "}"
            "QTableCornerButton::section {"
            "background-color: #F7F9FC;"
            "border: 1px solid #D3D3D3;"
            "}"
            "QHeaderView::section:horizontal {"
            "background-color: #2C3E50;"
            "color: white;"
            "border-radius: 5px;"
            "}"
            "QHeaderView::section:vertical {"
            "background-color: #F7F9FC;"
            "color: #333;"
            "border-radius: 5px;"
            "}"
        "")
        
        # Load Data
        self.load_data()
        
        content_layout.addLayout(search_layout)
        content_layout.addWidget(self.table)
        
        # Add content to splitter
        content_frame = QFrame()
        content_frame.setLayout(content_layout)
        self.splitter.addWidget(content_frame)
        
        main_layout.addWidget(self.splitter)
        self.setLayout(main_layout)
        
        # Sidebar Animation
        self.animation = QPropertyAnimation(self.sidebar_frame, b"maximumWidth")
    
    def toggle_menu(self):
        if self.side_menu.maximumWidth() == 200:
            self.animation.setDuration(300)
            self.animation.setStartValue(200)
            self.animation.setEndValue(0)
        else:
            self.animation.setDuration(300)
            self.animation.setStartValue(0)
            self.animation.setEndValue(200)
        self.animation.start()
    
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
            cover_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #333;")
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
