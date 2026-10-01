# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
vraag1 = input ("wat vind je van de huidige regering? ")
vraag2 = input ("wat vind je van de Python-lessen tot nu toe?")
vraag3 = input ("wat vind jij de mooiste stad van Nederlanf?")

bestand = open ("resultaten.txt" , "w")
bestand.write(f"Vraag 1: {vraag1}\n")
bestand.write(f"Vraag 2: {vraag2}\n")
bestand.write(f"Vraag 3: {vraag3}\n")
bestand.close()