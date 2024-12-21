from robot import *

droite()

for i in range(5):
    bas()
    while not surObjet():
        gauche()
    ramasser()
    while not surTrou():
        droite()
    deposer()