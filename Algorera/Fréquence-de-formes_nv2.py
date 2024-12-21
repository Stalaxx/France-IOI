from robot import *

rond = 0
carre = 0

def check():
    global rond, carre
    for i in range(13):
        if surRond():
            rond += 1
        elif surCarre():
            carre += 1
        droite()

bas()
check()
for i in range(13):
    gauche()
for i in range(13):
    if rond > carre:
        if surRond():
            ramasser()
            haut()
            deposer()
            bas()
    elif rond < carre:
        if surCarre():
            ramasser()
            haut()
            deposer()
            bas()
    droite()