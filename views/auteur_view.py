from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem

class AuthorsView(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout
        layout = QVBoxLayout(self)

        # Create TableView
        self.table = QTableView()
        layout.addWidget(self.table)

        # Create model for table data
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Author Name", "Country", "Books Written"])

        # Sample author data
        authors_data = [
            [1, "J.K. Rowling", "UK", 10],
            [2, "George R.R. Martin", "USA", 5],
            [3, "Agatha Christie", "UK", 85],
            [4, "Haruki Murakami", "Japan", 14],
            [5, "Stephen King", "USA", 63]
        ]

        # Insert rows into the table model
        for row_data in authors_data:
            row_items = [QStandardItem(str(item)) for item in row_data]
            self.model.appendRow(row_items)

        # Apply model to table
        self.table.setModel(self.model)

        # Styling: Adjust column widths
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Hide vertical row numbers
        self.table.verticalHeader().setVisible(False)

        # Enable alternating row colors
        self.table.setAlternatingRowColors(True)

        # Enable row selection
        self.table.setSelectionBehavior(QTableView.SelectRows)

        self.setLayout(layout)
