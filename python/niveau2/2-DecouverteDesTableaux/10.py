nbEmplacements = int(input())

marchands = [0] * nbEmplacements

for i in range(nbEmplacements):
   marchands[int(input())] = i
   
for marchand in marchands:
   print(marchand)