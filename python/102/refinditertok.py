import re

text = "Hello, world! 123 456."

# Wyrażenie regularne dla różnych tokenów
pattern = r'\d+|[a-zA-Z]+|[.,!?]'

matches = re.finditer(pattern, text)

tokens = []
for match in matches:
    token = match.group()
    start, end = match.start(), match.end()
    print(f"Token: {token}, Pozycja: {start}-{end}")
    tokens.append(token)

print("Wszystkie tokeny:", tokens)
