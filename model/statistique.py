import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import Database

class Statistique:
    @staticmethod
    def compter_livres():
        """Retourne le nombre total de livres dans la bibliothèque"""
        db = Database()
        livres = db.get_collection("livres")
        count = livres.count_documents({})
        db.close_connection()
        return count

    @staticmethod
    def compter_abonnes():
        """Retourne le nombre total d'abonnés"""
        db = Database()
        abonnes = db.get_collection("abonnes")
        count = abonnes.count_documents({})
        db.close_connection()
        return count

    @staticmethod
    def compter_emprunts():
        """Retourne le nombre total d'emprunts en cours"""
        db = Database()
        emprunts = db.get_collection("emprunts")
        count = emprunts.count_documents({})
        db.close_connection()
        return count

# Test d'affichage des stats
if __name__ == "__main__":
    print(f"📚 Nombre de livres : {Statistique.compter_livres()}")
    print(f"👤 Nombre d'abonnés : {Statistique.compter_abonnes()}")
    print(f"📅 Nombre d'emprunts actifs : {Statistique.compter_emprunts()}")
