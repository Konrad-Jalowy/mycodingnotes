import re

pattern = r'\d+'  # Jedna lub więcej cyfr
text = "Znaleziono liczby 42 i 123 w tekście."

match = re.search(pattern, text)
if match:
    print(f"Dopasowanie: {match.group()}")  # Pierwsze dopasowanie
    print(f"Pozycja: {match.start()}-{match.end()}")  # Pozycja w tekście
else:
    print("Brak dopasowania")