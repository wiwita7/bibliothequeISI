import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import Database

class Auteur:
    def __init__(self, nom, nationalite):
        self.nom = nom
        self.nationalite = nationalite

    def save(self):
        """Sauvegarder l'auteur dans MongoDB"""
        db = Database()
        auteurs = db.get_collection("auteurs")
        auteurs.insert_one(self.__dict__)  # Insère les données dans MongoDB
        db.close_connection()
        print(f"🖊️ Auteur '{self.nom}' ajouté avec succès !")

# Test d'ajout
if __name__ == "__main__":
    auteur = Auteur("Victor Hugo", "Français")
    auteur.save()
