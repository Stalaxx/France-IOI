nbLivres = int(input())
longueurMinimale = int(input())

for i in range(nbLivres):
    titre = input()
    description = input()

    if (len(description) < longueurMinimale):
        print(titre)
        

