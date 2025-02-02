from pymongo import MongoClient
from config import MONGO_URI

def get_database():
    client = MongoClient(MONGO_URI)
    return client["bibliotheque"]  # Nom de la base de données

db = get_database()
users_collection = db["users"]  # Collection des utilisateurs