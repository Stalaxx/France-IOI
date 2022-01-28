nbLignes = int(input())

for i in range(nbLignes):
    ligne = input()
    tailleLigne = len(ligne)
    for j in range(tailleLigne):
        print(ligne[tailleLigne - 1 - j], end="")
    print()
