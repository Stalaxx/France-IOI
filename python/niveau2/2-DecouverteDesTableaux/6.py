nbDeplacements = int(input())

deplacements = [0] * nbDeplacements

for i in range(nbDeplacements):
   deplacements[i] = int(input())
   
for i in range(nbDeplacements - 1, -1, -1):
   deplacement = deplacements[i]
   if (deplacement == 1):
      print(2)
   elif (deplacement == 2):
      print(1)
   elif (deplacement == 4):
      print(5)
   elif (deplacement == 5):
      print(4)
   elif (deplacement == 3):
      print(3)