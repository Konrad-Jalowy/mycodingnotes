import re

pattern = r'\w+(?=:)'  # Słowo, za którym stoi dwukropek
text = "Produkt: 123, Cena: 456"

matches = re.findall(pattern, text)
print(matches)  # Output: ['Produkt', 'Cena']
