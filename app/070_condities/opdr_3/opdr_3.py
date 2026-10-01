# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd_input = int(input("Voer uw leeftijd in: "))

for groep in leeftijd:
    minimum = leeftijd [groep][0]
    maximum = leeftijd [groep][1]

    if minimum <= leeftijd_input <= maximum:
        korting = kortings_percentages[groep]
        prijs = normale_toegangsprijs * (1 - korting / 100)

        print("U behoort tot de groep", groep)
        print("U krijgt", korting, "% korting")
        print("U betaalt daarom", prijs)
