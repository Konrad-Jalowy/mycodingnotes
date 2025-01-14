import re

# Dopasowanie liczb NIE poprzedzonych znakiem "$"
pattern = r'(?<!\$)\b\d+\b'
text = "$100, €200, $300"

matches = re.findall(pattern, text)
print(matches)  # Output: ['200']
