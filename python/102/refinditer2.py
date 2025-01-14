import re
pattern = r'\w+\s\d+'  # Słowo i liczba
text = "Produkt 123, Cena 456."

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Dopasowanie: {match.group()}, Pozycja: {match.start()}-{match.end()}")
# Dopasowanie: Produkt 123, Pozycja: 0-11
# Dopasowanie: Cena 456, Pozycja: 13-21