# Connexion à MongoDB
from pymongo import MongoClient
import configparser

# Lire la configuration depuis config.ini
config = configparser.ConfigParser()
config.read("config.ini")

MONGO_URI = config.get("database", "MONGO_URI")

class Database:
    def __init__(self):
        """Connexion à MongoDB Atlas"""
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client["bibliotheque"]  # Remplace par le nom de ta base
            print("✅ Connexion réussie à MongoDB Atlas !")
        except Exception as e:
            print(f"❌ Erreur de connexion : {e}")

    def get_collection(self, collection_name):
        """Récupérer une collection"""
        return self.db[collection_name]

    def close_connection(self):
        """Fermer la connexion"""
        self.client.close()
        print("🔌 Connexion MongoDB fermée.")

# Test de connexion
if __name__ == "__main__":
    db = Database()
    livres = db.get_collection("livres")
    print(f"📚 Nombre de livres : {livres.count_documents({})}")
    db.close_connection()