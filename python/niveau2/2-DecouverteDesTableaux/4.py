nbProduits = int(input())
produits = [0]*nbProduits
nbPersonnes = int(input())

for i in range(nbPersonnes):
   numProduitPref = int(input())
   produits[numProduitPref] += 1
   
for produit in produits :
   print(produit)
   