from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QComboBox
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Signal, Qt, QPoint
import base64
from pymongo import MongoClient
from views.modifyBook import Ui_DialogModify  # Interface générée

class ModifyBookWindow(QDialog):
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
        self.ui = Ui_DialogModify()
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
        """ Update the book in MongoDB instead of adding a new one """
        titre = self.ui.title_input.text().strip()
        auteur = self.ui.author_input.text().strip()
        isbn = self.ui.isbn_input.text().strip()
        description = self.ui.description_input.toPlainText().strip()
        categorie = self.ui.category_input.currentText()
        disponibilite = self.ui.availability_input.currentText()
        nombre_exemplaires = self.ui.number_of_copies_input.value()

        # Ensure all required fields are filled
        if not titre or not auteur or not isbn:
            self.show_error_message("Please fill all required fields.")
            return

        # Ensure year is a number
        annee = self.ui.year_input.text().strip()
        try:
            annee = int(annee)
        except ValueError:
            self.show_error_message("The year should be in numbers")
            return

        # Convert cover image to Base64 if changed
        couverture_base64 = None
        if self.cover_image_path:
            with open(self.cover_image_path, "rb") as img_file:
                couverture_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        # Prepare book data for update
        updated_book = {
            "titre": titre,
            "auteur": auteur,
            "ISBN": isbn,
            "annee_publication": annee,
            "categorie": categorie,
            "disponible": disponibilite.lower() == "true",
            "description": description,
            "nombre_exemplaires": nombre_exemplaires,
        }

        # Add cover image only if it's changed
        if couverture_base64:
            updated_book["couverture"] = couverture_base64

        # Ensure we have a valid book ID for updating
        if hasattr(self, "book_id") and self.book_id:
            from bson.objectid import ObjectId
            result = self.books_collection.update_one(
                {"_id": ObjectId(self.book_id)},
                {"$set": updated_book}
            )
            
            if result.modified_count > 0:
                print(f"✅ Book {self.book_id} updated successfully!")
                self.book_added.emit(updated_book)  # Notify the table to refresh
                self.accept()  # Close the window
            else:
                self.show_error_message("No changes were made or update failed")
        else:
            self.show_error_message("Book ID not found for update")
        
    def show_error_message(self, message):
        """ Affiche un message d'erreur dans une fenêtre """
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Erreur")
        error_dialog.setText(message)
        error_dialog.exec()

    def populate_fields(self, book):
        """ Populate the fields with existing book data """
        self.book_id = str(book["_id"])  # Store book ID for updating
        self.ui.title_input.setText(book.get("titre", ""))
        self.ui.author_input.setText(book.get("auteur", ""))
        self.ui.isbn_input.setText(book.get("ISBN", ""))
        self.ui.year_input.setText(str(book.get("annee_publication", "")))
        self.ui.category_input.setCurrentText(book.get("categorie", ""))
        self.ui.availability_input.setCurrentText("True" if book.get("disponible", False) else "False")
        self.ui.description_input.setPlainText(book.get("description", ""))
        self.ui.number_of_copies_input.setValue(book.get("nombre_exemplaires", 1))

        # Load cover image if available
        couverture_base64 = book.get("couverture", None)
        if couverture_base64:
            pixmap = QPixmap()
            pixmap.loadFromData(base64.b64decode(couverture_base64))
            self.ui.image_label.setPixmap(pixmap.scaled(120, 180))
