from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class HelpView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("<h1>📖 Aide - Gestion de la Bibliothèque</h1>")
        instructions = QLabel("""
        <h3>📌 Guide d'utilisation :</h3>
        ➤ Ajouter un livre : Allez à la page "Books" et cliquez sur "Ajouter".<br>
        ➤ Gérer les emprunts : Allez à "Loans" et ajoutez un nouvel emprunt.<br>
        ➤ Voir les abonnés : Allez à "Subscribers".<br>
        ➤ Rechercher un livre : Utilisez la barre de recherche.<br>
        """)

        layout.addWidget(title)
        layout.addWidget(instructions)
        self.setLayout(layout)
