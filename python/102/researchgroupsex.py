import re
pattern = r'(\w+)\s(\d+)'  # Słowo, spacja, liczba
text = "Produkt 123, Cena 456."

match = re.search(pattern, text)
if match:
    print(f"Całość: {match.group(0)}")  # Cały dopasowany tekst
    print(f"Grupa 1: {match.group(1)}")  # Pierwsza grupa (słowo)
    print(f"Grupa 2: {match.group(2)}")  # Druga grupa (liczba)
# Całość: Produkt 123
# Grupa 1: Produkt
# Grupa 2: 123
