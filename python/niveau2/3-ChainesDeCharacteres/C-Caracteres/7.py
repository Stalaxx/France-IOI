ligne = list(input())

for i in range(len(ligne)):
    if (ligne[i] == ' '):
        ligne[i] = '_'

print("".join(ligne)) 


