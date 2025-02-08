from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QHeaderView, QAbstractItemView
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class EmployeeTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Dashboard")
        self.setGeometry(100, 100, 900, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Création du QTableView
        self.table = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["#", "Nom", "Code", "Poste", "Téléphone", "Date d'entrée"])
        self.table.setModel(self.model)

        # Ajouter des données
        employees = [
            ["1", "Jimmy Henderson", "CU009", "Angular Developer", "788-998-1643", "Mar 27, 2016"],
            ["2", "Eva W Ramirez", "CU012", "Front-end Developer", "603-801-5810", "Jul 02, 2016"],
            ["3", "Benrita Stubbs", "CU081", "Graphic Designer", "434-709-1874", "Dec 12, 2017"],
            ["4", "Terrell Elliott", "CU034", "Mean Developer", "318-225-1064", "Apr 12, 2017"],
        ]

        for row in employees:
            self.model.appendRow([QStandardItem(item) for item in row])

        # Ajuster la hauteur des lignes
        self.table.verticalHeader().setDefaultSectionSize(50)

        # Désactiver l'édition
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Ajuster automatiquement la largeur des colonnes sauf la dernière
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Ajouter un bouton pour étendre la dernière colonne
        self.expand_button = QPushButton("🔍 Agrandir dernière colonne")
        self.expand_button.clicked.connect(self.expand_last_column)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.expand_button)
        layout.addWidget(self.table)
        self.central_widget.setLayout(layout)

    def expand_last_column(self):
        """Agrandit la dernière colonne pour occuper tout l'espace disponible"""
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)


# Lancer l'application
app = QApplication([])
window = EmployeeTable()
window.show()
app.exec()
