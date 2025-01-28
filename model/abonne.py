import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import Database

class Abonne:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def save(self):
        """Sauvegarder l'abonné dans MongoDB"""
        db = Database()
        abonnes = db.get_collection("abonnes")
        abonnes.insert_one(self.__dict__)  # Insère les données dans MongoDB
        db.close_connection()
        print(f"👤 Abonné '{self.nom}' ajouté avec succès !")

# Test d'ajout
if __name__ == "__main__":
    abonne = Abonne("Jean Dupont", "jean.dupont@email.com")
    abonne.save()
