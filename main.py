import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model.Livre import Livre


if __name__ == "__main__":
    # Ajouter un livre
    livre = Livre("Les Misérables", "Victor Hugo", 1862)
    livre.save()

    # Afficher tous les livres
    print("📚 Liste des livres :")
    livres = Livre.get_all()
    for livre in livres:
        print(livre)

    # Mettre à jour un livre
    Livre.update("Les Misérables", {"annee": 1870})
    print("📚 Après mise à jour :", Livre.get_all())

    # Supprimer un livre
    Livre.delete("Les Misérables")
    print("📚 Après suppression :", Livre.get_all())
