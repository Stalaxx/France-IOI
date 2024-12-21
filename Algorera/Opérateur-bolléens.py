from robot import *

for i in range(8):
    haut()
    for i in range(14):
        droite()
        if (colonneRobot() >= 7 and colonneRobot() <=9):
            peindreCase()
            
        if (ligneRobot() >= 4 and ligneRobot() <=5):
            peindreCase()
    for i in range(14):
        gauche()