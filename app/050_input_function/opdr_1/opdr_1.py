# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math


a = int(input("Geef de lengte van zijde :  "))
b = int(input("Geef de lengte van zijde : "))

c = math.sqrt(a ** 2 + b ** 2)

print(f"De schuine zijde is: {c}")
