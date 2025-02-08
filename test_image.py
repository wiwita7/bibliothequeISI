import base64
import io
from pymongo import MongoClient
from PIL import Image

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bibliotheque_universitaire"]
books_collection = db["books"]

# Récupérer un livre avec une couverture
book = books_collection.find_one({"titre": "Apprendre Python 3"})

if book and "couverture" in book:
    image_data = base64.b64decode(book["couverture"])
    image = Image.open(io.BytesIO(image_data))

    # Afficher l'image
    image.show()
else:
    print("❌ Aucune couverture trouvée pour ce livre.")
