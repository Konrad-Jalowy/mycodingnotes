import re
pattern = r'\d+'  # Liczby
text = "Usuń liczby: 42, 123."

result = re.sub(pattern, '***', text)
print(result)  # Usuń liczby: ***, ***.
