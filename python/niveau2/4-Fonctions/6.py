def NombreSuivant(terme):
    if (terme % 2 == 0):
        return terme // 2
    else:
        return terme * 3 + 1


nb = int(input())

while (nb != 1):
    nb = NombreSuivant(nb)
    print(nb, end=" ")



