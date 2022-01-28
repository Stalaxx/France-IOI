nbOperations = int(input())
ingredients = [0] * 10

for i in range(nbOperations):
   numIngredient = int(input()) - 1
   quantite = int(input())
   ingredients[numIngredient] += quantite
   
   
for ingredient in ingredients:
   print(ingredient)