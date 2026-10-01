# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

prompt = "Raad mijn geheime getal \n"

geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

while True:
    gok = int(input(prompt))
    aantal_pogingen += 1

    if gok < geheim_getal:
        print("Hoger")
    elif gok > geheim_getal:
        print("Lager")
    else:
        print("Goed geraden!")
        print("Het geheime getal was:", geheim_getal)
        print("Aantal pogingen:", aantal_pogingen)
        break
