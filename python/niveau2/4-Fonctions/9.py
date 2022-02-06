def MetresVersPieds(nbMetres):
    return nbMetres * 1 / 0.3048

def GrammesVersLivres(nbGrammes):
    return nbGrammes * 0.002205

def CelsiusVersFahrenheit(nbCelsius):
    return 32 + 1.8 * nbCelsius 


nbConversions = int(input())

for i in range(nbConversions):
    entrees = input().split(' ')

    mesure =  float(entrees[0])
    
    if (entrees[1] == "m"):
        print(MetresVersPieds(mesure), " p")
    elif (entrees[1] == "g"):
        print(GrammesVersLivres(mesure), " l")
    elif (entrees[1] == "c"):
        print(CelsiusVersFahrenheit(mesure), " f")




