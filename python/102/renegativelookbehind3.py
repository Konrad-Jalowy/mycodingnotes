import re

# Poprawiony wzorzec: Liczby NIE poprzedzone literą
pattern = r'(?<![a-zA-Z])\b\d+\b'
text = "A123 456 B789 012"

matches = re.findall(pattern, text)
print(matches)  # Output: ['456', '012']

