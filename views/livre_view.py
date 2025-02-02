from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem

class BooksView(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout(self)

        # Création du TableView
        self.table = QTableView()
        layout.addWidget(self.table)

        # Création du modèle de données
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Titre", "Auteur", "Genre", "Disponibilité"])

        # 📚 Exemple de livres dans la bibliothèque
        books_data = [
            [1, "Harry Potter", "J.K. Rowling", "Fantasy", "Disponible"],
            [2, "Game of Thrones", "George R.R. Martin", "Fantasy", "Emprunté"],
            [3, "Les Misérables", "Victor Hugo", "Classique", "Disponible"],
            [4, "1984", "George Orwell", "Science-fiction", "Disponible"],
            [5, "Le Petit Prince", "Antoine de Saint-Exupéry", "Conte", "Disponible"]
        ]

        # Ajouter les données au modèle
        for row_data in books_data:
            row_items = [QStandardItem(str(item)) for item in row_data]
            self.model.appendRow(row_items)

        # Appliquer le modèle à la table
        self.table.setModel(self.model)

        # 🛠️ Ajuster la taille des colonnes
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Cacher les numéros de ligne
        self.table.verticalHeader().setVisible(False)

        # Activer le
