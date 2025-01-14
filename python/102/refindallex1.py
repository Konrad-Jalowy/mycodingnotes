import re

pattern = r'\d+'  # Dopasowanie jednej lub więcej cyfr
text = "Znajdź liczby 42 i 123 w tym tekście."

matches = re.findall(pattern, text)
print(matches)  # Output: ['42', '123']
