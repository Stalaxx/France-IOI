nbLignes, nbMots = map(int, input().split(' '))

nbMotsParLongueur = [0] * 101

for i in range(nbLignes):
    mots = input().split(' ')
    for mot in mots:
        nbMotsParLongueur[len(mot)] += 1

for i in range(101):
    if (nbMotsParLongueur[i] != 0):
        print(i, " : ", nbMotsParLongueur[i])

