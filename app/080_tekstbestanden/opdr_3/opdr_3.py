# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

tekst = input("Geef de tekst die je wilt encrypten.. ")

encryptie = ""

for letter in tekst:
    if letter.isalpha():
        code = ord(letter)
        nieuwe_code = (code - ord('a') + 5) % 26 + ord('a')
        encryptie += chr(nieuwe_code)
    else:
        encryptie += letter

print(encryptie)