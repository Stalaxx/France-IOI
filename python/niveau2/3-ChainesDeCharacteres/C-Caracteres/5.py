cartesJ1 = input()
cartesJ2 = input()

nbCartesJ1 = len(cartesJ1)
nbCartesJ2 = len(cartesJ2)

i = 0
while (i < nbCartesJ1 and i < nbCartesJ2 
    and cartesJ1[i] == cartesJ2[i]):
    i += 1 

if (nbCartesJ1 == nbCartesJ2):
    if (i == nbCartesJ1):
        print("=")
    elif (cartesJ1[i] < cartesJ2[i]):
        print("1")
    else:
        print("2")
else:
    if (i == nbCartesJ1):
        print("2")
    elif (i == nbCartesJ2):
        print("1")
    elif (cartesJ1[i] < cartesJ2[i]):
        print("1")
    else:
        print("2")

print(i)