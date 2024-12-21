from robot import *

def left():
    peindreCase()
    gauche()
    peindreCase()
    gauche()
    movePaint(1)
    peindreCase()
    droite()
    droite()
    bas()
def right():
    peindreCase()
    droite()
    peindreCase()
    droite()
    movePaint(1)
    peindreCase()
    gauche()
    gauche()
    bas()

def movePaint(v):
    for i in range(v):
        peindreCase()
        haut()
    
def full(v):
    for i in range(v):
        droite()
    movePaint(2)
    left()
    movePaint(2)
    right()
    
    movePaint(3)
    right()
    movePaint(2)
    left()
    movePaint(2)
    
    for i in range(11):
        bas()

full(3)
full(8)
full(6)