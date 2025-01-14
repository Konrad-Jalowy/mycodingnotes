import re

# Wzorzec: Nazwy plików poprzedzone "file:"
pattern = r'(?<=file:)\w+\.\w+'
text = "file:example.txt file:test.png url:other.jpg"

matches = re.findall(pattern, text)
print(matches)  # Output: ['example.txt', 'test.png']
