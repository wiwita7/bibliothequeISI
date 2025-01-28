import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import Database


class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def save(self):
        """Sauvegarder le livre dans MongoDB"""
        db = Database()
        livres = db.get_collection("livres")
        livres.insert_one(self.__dict__)  # Insère les données dans MongoDB
        db.close_connection()
        print(f"📖 Livre '{self.titre}' ajouté avec succès !")

    @staticmethod
    def get_all():
        """Récupérer tous les livres"""
        db = Database()
        livres = db.get_collection("livres")
        result = list(livres.find({}, {"_id": 0}))  # Récupérer tous les livres sans `_id`
        db.close_connection()
        return result
    @staticmethod
    def update(titre, nouveaux_donnees):
        """Mettre à jour un livre"""
        db = Database()
        livres = db.get_collection("livres")
        result = livres.update_one({"titre": titre}, {"$set": nouveaux_donnees})
        db.close_connection()
        if result.matched_count:
            print(f"✅ Livre '{titre}' mis à jour avec succès !")
        else:
            print(f"❌ Livre '{titre}' non trouvé.")

    @staticmethod
    def delete(titre):
        """Supprimer un livre"""
        db = Database()
        livres = db.get_collection("livres")
        result = livres.delete_one({"titre": titre})
        db.close_connection()
        if result.deleted_count:
            print(f"🗑️ Livre '{titre}' supprimé avec succès !")
        else:
            print(f"❌ Livre '{titre}' non trouvé.")

