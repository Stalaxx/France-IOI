prixAuKilo = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
prixTotal = 0

for i in range(10):
   poids = int(input())
   prixTotal += poids * prixAuKilo[i]
   
print(prixTotal)