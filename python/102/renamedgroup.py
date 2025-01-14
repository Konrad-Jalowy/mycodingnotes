import re

pattern = r'(?P<word>\w+): (?P<number>\d+)'
text = "Produkt: 123"

match = re.search(pattern, text)
if match:
    print(f"Słowo: {match.group('word')}")  # Output: Produkt
    print(f"Liczba: {match.group('number')}")  # Output: 123
