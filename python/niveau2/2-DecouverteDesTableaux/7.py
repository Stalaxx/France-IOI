nbHabitants = int(input())

fortunes = [0] * nbHabitants

for i in range(nbHabitants):
   fortunes[i] = int(input())
   
fortunes.sort()

fortuneMediane = 0
indiceMoyen = (nbHabitants - 1) // 2
if (nbHabitants % 2 == 1):
   fortuneMediane = fortunes[indiceMoyen ]   
else :
   fortuneMediane = (fortunes[indiceMoyen ] + fortunes[indiceMoyen + 1]) / 2
   
print(fortuneMediane)