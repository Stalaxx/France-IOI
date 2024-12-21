from robot import *

droite()
nb = nombreSurCase()

droite()
bas()

temp = 0
for i in range(nb):
    peindreCase()
    
    for i in range(temp):
        droite()
        peindreCase()

    for i in range(temp):
        gauche()
    bas()
    temp += 1