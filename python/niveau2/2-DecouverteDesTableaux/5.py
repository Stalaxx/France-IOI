nbCharrettes = int(input())

poids = [0.0] * nbCharrettes 
poidsTotal = 0.0

for i in  range(nbCharrettes):
   poids[i] = float(input())
   poidsTotal += poids[i]
   
   
poidsMoyen = poidsTotal / nbCharrettes
   
for poidsCharrette in poids:
   print(poidsMoyen - poidsCharrette)