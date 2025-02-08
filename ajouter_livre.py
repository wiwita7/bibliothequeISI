from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Signal, Qt, QPoint
import base64
from pymongo import MongoClient
from views.addBook import Ui_Dialog  # Interface générée

class AddBookWindow(QDialog):
    book_added = Signal(dict)  # Signal pour informer le tableau

    def __init__(self):
        super().__init__()

        # Connexion MongoDB avec gestion d'erreur
        try:
            self.db = MongoClient("mongodb://localhost:27017/")["Library_db"]
            self.books_collection = self.db["books"]
            print("✅ Connexion à MongoDB réussie")
        except Exception as e:
            self.show_error_message(f"Erreur de connexion à MongoDB: {e}")

        # Charger l'interface Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Ajouter les catégories au QComboBox
        categories = [
            "Informatique", 
            "Mathématiques & Statistiques", 
            "Sciences et Ingénierie",
            "Économie et Gestion", 
            "Littérature et Langues", 
            "Médecine et Santé"
        ]
        self.ui.category_input.addItems(categories)
        
        # Ajouter les options de disponibilité au QComboBox
        self.availability = ["True", "False"]
        self.ui.availability_input.addItems(self.availability)
        self.ui.availability_input.setCurrentText("True")
        
        # Connexion des boutons
        self.ui.save_btn.clicked.connect(self.save_book)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.add_image_btn.clicked.connect(self.select_cover_image)
        self.ui.close_btn.clicked.connect(self.close)

        # Variables
        self.cover_image_path = None
        # Window Configurations
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Dragging variables
        self.dragging = False
        self.offset = QPoint()

    ### 🟢 IMPLEMENT DRAGGING FUNCTIONALITY
    def mousePressEvent(self, event: QMouseEvent):
        """ Capture the initial position when the mouse is pressed """
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        """ Move the window when dragging """
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """ Stop dragging when mouse is released """
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def select_cover_image(self):
        """ Ouvre un QFileDialog pour choisir une image """
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Book Cover", "", "Images (*.png *.jpg *.jpeg)")

        if file_path:
            self.cover_image_path = file_path
            pixmap = QPixmap(file_path)
            self.ui.image_label.setPixmap(pixmap.scaled(120, 180))
            self.ui.image_label.setText("")

    def save_book(self):
        """ Sauvegarde le livre dans MongoDB avec une couverture en Base64 et met à jour la TableView """
        titre = self.ui.title_input.text().strip()
        auteur = self.ui.author_input.text().strip()
        isbn = self.ui.isbn_input.text().strip()
        description = self.ui.description_input.toPlainText().strip()
        categorie = self.ui.category_input.currentText()
        disponibilite = self.ui.availability_input.currentText()
        nombre_exemplaires = self.ui.number_of_copies_input.value()

        # Vérification des champs obligatoires
        if not titre or not auteur or not isbn:
            self.show_error_message("Please fill all required fields.")
            return

        # Vérification de l'année
        annee = self.ui.year_input.text().strip()
        try:
            annee = int(annee)
        except ValueError:
            self.show_error_message("The year should be in numbers")
            return

        # Convertir l’image en Base64 si sélectionnée
        couverture_base64 = None
        if self.cover_image_path:
            with open(self.cover_image_path, "rb") as img_file:
                couverture_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        # Insérer dans MongoDB
        books = {
            "titre": titre,
            "auteur": auteur,
            "ISBN": isbn,
            "annee_publication": annee,
            "categorie": categorie,
            "disponible": disponibilite.lower() == "true",
            "description": description,
            "nombre_exemplaires": nombre_exemplaires,
            "couverture": couverture_base64
        }

        result = self.books_collection.insert_one(books)

        if result.inserted_id:
            print(f"✅ Livre ajouté avec ID: {result.inserted_id}")
            books["_id"] = str(result.inserted_id)  # Ajouter l'ID du document
            self.book_added.emit(books)  # Envoyer le signal
            self.accept()  # Fermer la fenêtre
        else:
            self.show_error_message("Échec de l'insertion")

    def show_error_message(self, message):
        """ Affiche un message d'erreur dans une fenêtre """
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Erreur")
        error_dialog.setText(message)
        error_dialog.exec()