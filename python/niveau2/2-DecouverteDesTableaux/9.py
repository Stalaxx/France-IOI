nbPositions = int(input())
nbChangementsPositions = int(input())

positions = [0] * nbPositions

for i in range(nbPositions):
   positions[i] = int(input())
   
for i in range(nbChangementsPositions):
   index1 = int(input())
   index2 = int(input())   
   positions[index1], positions[index2] = positions[index2], positions[index1]


for numPersonne in positions:
   print(numPersonne)
   