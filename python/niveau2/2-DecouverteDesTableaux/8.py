nbParticipants = int(input())

nombres = [0] * nbParticipants

for i in range(nbParticipants):
   nombres[i] = int(input())
   
nombres.sort()

for i in range(nbParticipants // 2):
   print("{} {}".format(nombres[i], nombres[nbParticipants - 1 - i]))