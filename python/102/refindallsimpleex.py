import re
pattern = r'\d+'
text = "Liczby: 42, 123, 456."

matches = re.findall(pattern, text)
print(matches)  # ['42', '123', '456']

