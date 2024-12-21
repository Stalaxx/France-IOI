from robot import *

nbBilles = 0
droite()
while surBille():
    droite()
    nbBilles +=1
    
gauche()

for bille in range(nbBilles):
    while surBille():
        gauche()

    while not surBille():
        droite()

    ramasserBille()
    droite()

    while surBille():
        droite()
    
    deposerBille()
    gauche()
    while surBille():
        gauche()
