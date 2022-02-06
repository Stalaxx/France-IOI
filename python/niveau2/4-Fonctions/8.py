def AfficherLigne(nbCaracteres, motif):
    for i in range(nbCaracteres):
        print(motif, end="")

def AfficherColonne(nbCaracteres, motif):
    for i in range(nbCaracteres):
        print(motif)

def AfficherLigneAvecTrou(nbCaracteres, motif):
    print(motif, end="")
    AfficherLigne(nbCaracteres - 2, " ")
    print(motif, end="")


def AfficherRectangle(nbLignes, nbColonnes):
    if (nbLignes == 1):
        AfficherLigne(nbColonnes, "#")
    elif (nbColonnes ==  1):
        AfficherColonne(nbLignes, "#")
    else:
        AfficherLigne(nbColonnes, "#")
        print()
        
        for i in range(nbLignes - 2):
            AfficherLigneAvecTrou(nbColonnes, "#")
            print()

        AfficherLigne(nbColonnes, "#")

def AfficherTriangle(nbLignes):
    print("@")

    for i in range(nbLignes-2):
        AfficherLigneAvecTrou(i+2, "@")
        print()

    AfficherLigne(nbLignes, "@")


nbX = int(input())
AfficherLigne(nbX, "X")
print()
print()

nbLignesRect = int(input())
nbColonnesRect = int(input())
AfficherRectangle(nbLignesRect, nbColonnesRect)
print()

nbLignesTriangles = int(input())
AfficherTriangle(nbLignesTriangles)
