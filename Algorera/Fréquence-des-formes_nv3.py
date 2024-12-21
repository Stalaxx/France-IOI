from robot import *

compteurs = [0, 0, 0, 0, 0, 0]

bas()

for i in range(13):
    index = 0 if surObjetPlein() else 3
    if surRond():
        compteurs[index] += 1
    elif surCarre():
        compteurs[index + 1] += 1
    else:
        compteurs[index + 2] += 1
    droite()
    
max_index = 0
for i in range(1, 6):
    if compteurs[i] > compteurs[max_index]:
        max_index = i
    

for i in range(13):
    gauche()
    index = 0 if surObjetPlein() else 3
    if surCarre():
        index += 1
    elif surTriangle():
        index += 2
    
    if (max_index == index):
        ramasser()
        haut()
        deposer()
        bas()