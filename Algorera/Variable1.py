from robot import *

droite()
droite()

temp = 0
for i in range(5):
    for i in range(5):
        temp += nombreCase()
        droite()
    droite()
    ecrireNombre(temp)
    temp = 0
    bas()
    for i in range(6):
        gauche()


