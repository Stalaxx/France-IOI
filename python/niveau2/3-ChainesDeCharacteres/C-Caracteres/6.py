lettreCherchee = input()
nbLignes = int(input())

nbApparitions = 0

for i in range(nbLignes):
    ligne = input()
    for caractere in ligne:
        if (caractere == lettreCherchee):
            nbApparitions += 1

print(nbApparitions)

