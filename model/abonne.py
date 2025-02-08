from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QFrame, QListWidget, QListWidgetItem, QDialog, QLineEdit, QFormLayout, QMessageBox, QComboBox, QLineEdit
from PySide6.QtGui import QFont, QPainter
from PySide6.QtCore import Qt
import sys
from PySide6.QtCharts import QChart, QChartView, QPieSeries

class AddPlanDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Plan")
        self.setGeometry(300, 300, 400, 300)
        
        layout = QFormLayout()
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.year_input = QLineEdit()
        self.availability_input = QLineEdit()
        self.status_input = QComboBox()
        self.status_input.addItems(["New", "In Progress", "Completed"])
        
        layout.addRow("Title:", self.title_input)
        layout.addRow("Author:", self.author_input)
        layout.addRow("Year of Publishing:", self.year_input)
        layout.addRow("Availability (copies):", self.availability_input)
        layout.addRow("Status:", self.status_input)
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_and_save)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addRow(button_layout)
        self.setLayout(layout)
    
    def validate_and_save(self):
        if not self.title_input.text() or not self.author_input.text() or not self.year_input.text().isdigit() or not self.availability_input.text().isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter valid details.")
        else:
            self.accept()

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard UI")
        self.setGeometry(100, 100, 1200, 700)

        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(80)
        self.sidebar.setStyleSheet("background-color: #2C3E50; border-radius: 10px;")
        sidebar_layout = QVBoxLayout(self.sidebar)

        icons = ["🏠", "📁", "🔍", "⚙️", "🔓"]
        for icon in icons:
            btn = QPushButton(icon)
            btn.setStyleSheet("color: white; font-size: 18px; padding: 10px; border: none;")
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch()

        self.content = QWidget()
        content_layout = QVBoxLayout(self.content)

        self.header = QHBoxLayout()
        self.title = QLabel("📋 My Plans")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.add_button = QPushButton("+ Add Plan")
        self.add_button.setStyleSheet("background-color: #3498db; color: white; padding: 5px 10px; border-radius: 5px;")
        self.add_button.clicked.connect(self.open_add_plan_dialog)
        self.header.addWidget(self.title)
        self.header.addStretch()
        self.header.addWidget(self.add_button)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.filter_table)
        content_layout.addWidget(self.search_input)
        
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["Plan Name", "Author", "Year", "Category", "Availability", "Status"])
        self.table.setStyleSheet("QTableWidget { border: none; font-size: 14px; }")
        
        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 5px 10px; border-radius: 5px;")
        self.delete_button.clicked.connect(self.delete_selected_row)
        
        self.update_button = QPushButton("Update Selected")
        self.update_button.setStyleSheet("background-color: #f39c12; color: white; padding: 5px 10px; border-radius: 5px;")
        self.update_button.clicked.connect(self.update_selected_row)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.update_button)
        content_layout.addLayout(button_layout)
        
        self.chart_view = self.create_statistics_chart()
        content_layout.addWidget(self.chart_view)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content)

        self.setCentralWidget(main_widget)
    
    def filter_table(self):
        search_text = self.search_input.text().lower()
        for row in range(self.table.rowCount()):
            match = any(search_text in self.table.item(row, col).text().lower() for col in range(self.table.columnCount()) if self.table.item(row, col))
            self.table.setRowHidden(row, not match)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
