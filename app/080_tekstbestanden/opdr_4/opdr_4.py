vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

voornaam = input("1. " + vragen[0] + "\n")
achternaam = input("2. " + vragen[1] + "\n")
drank = input("3. " + vragen[2] + "\n")
eten = input("4. " + vragen[3] + "\n")

feestganger = {
    "voornaam": voornaam,
    "achternaam": achternaam,
    "drank": drank,
    "eten": eten
}

with open("feestgangers.txt", "a") as bestand:
    bestand.write("----\n")
    bestand.write("voornaam: " + feestganger["voornaam"] + "\n")
    bestand.write("achternaam: " + feestganger["achternaam"] + "\n")
    bestand.write("drank: " + feestganger["drank"] + "\n")
    bestand.write("eten: " + feestganger["eten"] + "\n")

print()
print("Bedankt voor het invullen!")
print("See you at the party.")