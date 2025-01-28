import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import Database
from datetime import datetime, timedelta

class Emprunt:
    def __init__(self, id_abonne, id_livre, date_emprunt=None, date_retour=None):
        self.id_abonne = id_abonne
        self.id_livre = id_livre
        self.date_emprunt = date_emprunt if date_emprunt else datetime.now()
        self.date_retour = date_retour if date_retour else self.date_emprunt + timedelta(days=14)  # 14 jours par défaut

    def save(self):
        """Sauvegarder l'emprunt dans MongoDB"""
        db = Database()
        emprunts = db.get_collection("emprunts")
        emprunts.insert_one(self.__dict__)  # Insère les données dans MongoDB
        db.close_connection()
        print(f"📅 Emprunt enregistré (Abonné: {self.id_abonne}, Livre: {self.id_livre})")

# Test d'ajout
if __name__ == "__main__":
    emprunt = Emprunt("65d8a4b2e1f43", "65d8a4b2e1f76")  # Remplacer par des ID valides
    emprunt.save()
