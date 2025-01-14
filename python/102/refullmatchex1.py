import re
pattern = r'\d+'  # Tylko liczby
text = "12345"

if re.fullmatch(pattern, text):
    print("Cały tekst pasuje do wzorca.")
else:
    print("Brak pełnego dopasowania.")
