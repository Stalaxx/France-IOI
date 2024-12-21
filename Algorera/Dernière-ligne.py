from robot import *

matrix = [
    [],
    [],
    []
]

for row in range(3):
    for col in range(15):
        if surCaseMarquee():
            matrix[row].append(1)
        else:
            matrix[row].append(0)
        droite()
    bas()
    for _ in range(15):
        gauche()
        
for row in range(15):
    if matrix[0][row] + matrix[1][row] + matrix[2][row] >= 2:
        peindreCase()
    droite()
