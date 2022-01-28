nbLivres = int(input())

longueurDernierLivreLu = 0

for i in range(nbLivres):
    titre = input()
    longueurTitre = len(titre)

    if (longueurTitre > longueurDernierLivreLu):
        print(titre)
        longueurDernierLivreLu = longueurTitre
