import re

def custom_finditer(pattern, text, flags=0):
    """
    Minimalistyczny generator podobny do re.finditer.
    Zwraca dopasowane teksty i ich pozycje w oryginalnym ciągu.
    """
    pos = 0  # Aktualna pozycja w tekście
    while pos < len(text):
        match = re.search(pattern, text[pos:], flags)
        if not match:
            break
        # Oblicz dopasowanie w pełnym tekście
        start = pos + match.start()
        end = pos + match.end()
        yield match.group(), start, end
        pos = end  # Przesuń wskaźnik za ostatnie dopasowanie

# Testowanie custom_finditer
pattern = r'\d+'
text = "Liczby: 42, 123, 456."

for value, start, end in custom_finditer(pattern, text):
    print(f"Dopasowanie: '{value}', Start: {start}, Koniec: {end}")
#Dopasowanie: '42', Start: 8, Koniec: 10
#Dopasowanie: '123', Start: 12, Koniec: 15
#Dopasowanie: '456', Start: 17, Koniec: 20