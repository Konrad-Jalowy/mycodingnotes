import re

# Wzorzec: Liczby poprzedzone symbolem $
pattern = r'(?<=\$)\d+'
text = "$100, €200, $300"

matches = re.findall(pattern, text)
print(matches)  # Output: ['100', '300']
