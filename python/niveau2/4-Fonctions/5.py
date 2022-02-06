def min2(a, b):
    if (a < b):
        return a
    else:
        return b

minimum = int(input())
for i in range(9):
    nb = int(input())
    minimum = min2(nb, minimum)

print(minimum)

