from robot import *

counts = [0] * 6
target_col = 1
most_frequent_index = 0

def calculate_goal():
    goal = colonne() - target_col
    if goal > 0:
        for _ in range(goal):
            gauche()
    elif goal < 0:
        for _ in range(-goal):
            droite()

def update_most_frequent():
    global most_frequent_index
    for i in range(6):
        if counts[i] > counts[most_frequent_index]:
            most_frequent_index = i

bas()

for _ in range(15):
    group = 0 if surObjetPlein() else 3
    if surRond():
        counts[group] += 1
    elif surCarre():
        counts[group + 1] += 1
    else:
        counts[group + 2] += 1
    droite()

for _ in range(5):
    calculate_goal()
    update_most_frequent()

    for _ in range(colonne() - 1):
        gauche()

    while counts[most_frequent_index] != 0:
        droite()
        if colonne() == 16:
            for _ in range(colonne() - 1):
                gauche()
        
        if surObjet():
            group = 0 if surObjetPlein() else 3
            if surCarre():
                group += 1
            elif surTriangle():
                group += 2

            if most_frequent_index == group:
                ramasser()
                calculate_goal()
                haut()
                deposer()
                bas()
                target_col += 1
                counts[most_frequent_index] -= 1
