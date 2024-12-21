from robot import *

def paint(v):
    for i in range(v):
        peindre()
        bas()

def mright(v):
    for i in range(v):
        droite()

def paintVer(v):
    for i in range(v):
        peindre()
        gauche()

def mbot(v):
    for i in range(v):
        bas()

def goToUp():
    for i in range(ligne()-1):
        haut()

def cote():
    for i in range(2):
        droite()
        mbot(5)
        paint(10)
        goToUp()
def cote2():
    for i in range(2):
        droite()
        paint(3)
        mbot(2)
        paint(2)
        mbot(5)
        paint(2)
        goToUp()       

def cote3(a,b,c,d):
    droite()
    mbot(a)
    paint(b)
    mbot(c)
    paint(d)
    goToUp()
cote3(7,5,2,1)
cote3(5,7,2,1)
cote3(5,2,7,1)

cote()
cote2()

droite()
paint(7)
mbot(5)
paint(2)
goToUp()

cote2()
cote()

cote3(5,2,7,1)
cote3(5,7,2,1)
cote3(7,5,2,1)

droite()
mbot(15)

gauche()
paintVer(5)
for i in range(5):
    gauche()
paintVer(5)


