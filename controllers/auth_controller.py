from database.connection import users_collection

class AuthController:
    def authenticate(self, email, password):
        user = users_collection.find_one({"email": email, "password": password})
        return user is not None

    def reset_password(self, email):
        user = users_collection.find_one({"email": email})
        if user:
            print(f"Email de réinitialisation envoyé à {email}")
            return True
        return False
