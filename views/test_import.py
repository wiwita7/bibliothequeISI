
try:
    from controllers.auth_controller import AuthController
    print("Import réussi !")
except ModuleNotFoundError as e:
    print("Erreur :", e)
