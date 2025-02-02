from database.connection import users_collection

users_collection.insert_one({
    "email": "test@example.com",
    "password": "12345"
})

print("Utilisateur ajouté avec succès !")
