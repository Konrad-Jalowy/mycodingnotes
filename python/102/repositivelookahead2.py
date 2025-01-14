import re

pattern = r'\d+(?=\$)'  # Liczby, po których znajduje się znak "$"
text = "100$, 200€, 300$"

matches = re.findall(pattern, text)
print(matches)  # Output: ['100', '300']