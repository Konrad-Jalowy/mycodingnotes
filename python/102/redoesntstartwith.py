import re

# Wzorzec: Liczby, które NIE zaczynają się od litery
pattern = r'\b[^a-zA-Z]\d+\b'
text = "123 A123 456 B789 012"

matches = re.findall(pattern, text)
print(matches)  # Output: ['123', ' 456', ' 012']