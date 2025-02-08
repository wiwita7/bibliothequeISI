from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, 
    QComboBox, QTextEdit, QGroupBox, QFrame, QSizePolicy, QGridLayout
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import base64
import os
from pymongo import MongoClient


class AddBookWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add New Book")
        self.setFixedSize(600, 500)  # Taille ajustée
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #003366;
            }
            QLineEdit, QTextEdit, QComboBox {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
                background-color: white;
            }
            QPushButton {
                background-color: #003366;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005599;
            }
            QFrame {
                background-color: black transparent;
                border-radius: 8px;
                border: 2px solid #ddd;
                padding: 10px;
            }
            QGroupBox {
                border: 2px solid #003366;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
                color: #003366;
            }
        """)

        # Layout principal
        main_layout = QVBoxLayout()

        # Section Titre avec icône
        title_layout = QHBoxLayout()
        title_label = QLabel("📚 Add New Book")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: #003366; margin-bottom: 15px;")
        title_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Form Layout (Utilisation de QGridLayout pour bien aligner les champs)
        form_layout = QGridLayout()
        form_frame = QFrame()
        form_frame.setLayout(form_layout)

        # Champs du formulaire
        self.titre_input = QLineEdit()
        self.auteur_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.annee_input = QLineEdit()
        self.categorie_input = QComboBox()
        self.categorie_input.addItems(["Informatique", "Mathématiques", "CyberSécurité", "Développement Web", "Science des Données"])
        self.description_input = QTextEdit()
        self.description_input.setFixedHeight(50)  # Réduire la hauteur de la description
        self.exemplaires_input = QLineEdit()

        # Ajouter les widgets dans la grille
        form_layout.addWidget(QLabel("Title:"), 0, 0)
        form_layout.addWidget(self.titre_input, 0, 1)

        form_layout.addWidget(QLabel("Author:"), 1, 0)
        form_layout.addWidget(self.auteur_input, 1, 1)

        form_layout.addWidget(QLabel("ISBN:"), 2, 0)
        form_layout.addWidget(self.isbn_input, 2, 1)

        form_layout.addWidget(QLabel("Publication Year:"), 3, 0)
        form_layout.addWidget(self.annee_input, 3, 1)

        form_layout.addWidget(QLabel("Category:"), 4, 0)
        form_layout.addWidget(self.categorie_input, 4, 1)

        form_layout.addWidget(QLabel("Description:"), 5, 0)
        form_layout.addWidget(self.description_input, 5, 1)

        form_layout.addWidget(QLabel("Number of Copies:"), 6, 0)
        form_layout.addWidget(self.exemplaires_input, 6, 1)

        # Section Image
        image_group = QGroupBox("Book Cover")
        image_layout = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setFixedSize(120, 180)
        self.image_label.setStyleSheet("border: 1px solid #ccc; background-color: white;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setText("No Image")

        self.cover_button = QPushButton("Choose Image")
        self.cover_button.setFixedWidth(200)  # Réduire la largeur du bouton
        self.cover_button.clicked.connect(self.select_cover_image)

        image_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        image_layout.addWidget(self.cover_button, alignment=Qt.AlignCenter)
        image_group.setLayout(image_layout)

        # Boutons Actions
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("✔ Save")
        self.save_button.setFixedWidth(150)  # Fixer la largeur des boutons
        self.save_button.clicked.connect(self.save_book)

        self.cancel_button = QPushButton("✖ Cancel")
        self.cancel_button.setFixedWidth(150)
        self.cancel_button.clicked.connect(self.close)

        button_layout.addWidget(self.save_button, alignment=Qt.AlignRight)
        button_layout.addWidget(self.cancel_button, alignment=Qt.AlignLeft)

        # Ajout des composants au Layout Principal
        main_layout.addLayout(title_layout)
        main_layout.addWidget(form_frame)
        main_layout.addWidget(image_group, alignment=Qt.AlignCenter)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Variables
        self.cover_image_path = None
        self.db = MongoClient("mongodb://localhost:27017/")["bibliotheque_universitaire"]
        self.books_collection = self.db["books"]

    def select_cover_image(self):
        """ Ouvre un QFileDialog pour choisir une image et stocke son chemin """
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Choose Book Cover", "", "Images (*.png *.jpg *.jpeg)")

        if file_path:
            self.cover_image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(120, 180))
            self.image_label.setText("")

    def save_book(self):
        """ Sauvegarde le livre dans MongoDB avec une couverture en Base64 """
        titre = self.titre_input.text()
        auteur = self.auteur_input.text()
        isbn = self.isbn_input.text()
        annee = self.annee_input.text()
        categorie = self.categorie_input.currentText()
        description = self.description_input.toPlainText()
        exemplaires = self.exemplaires_input.text()

        if not titre or not auteur or not isbn:
            print("❌ Please fill all required fields.")
            return

        # Convertir l’image en Base64 si sélectionnée
        couverture_base64 = None
        if self.cover_image_path:
            with open(self.cover_image_path, "rb") as img_file:
                couverture_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        # Insérer dans MongoDB
        book = {
            "titre": titre,
            "auteur": auteur,
            "ISBN": isbn,
            "annee_publication": int(annee) if annee.isdigit() else 0,
            "categorie": categorie,
            "description": description,
            "nombre_exemplaires": int(exemplaires) if exemplaires.isdigit() else 1,
            "couverture": couverture_base64
        }

        self.books_collection.insert_one(book)
        print("✅ Book successfully added!")
        self.accept()
