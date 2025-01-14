import re

class CustomMatch:
    def __init__(self, match, offset=0):
        self._match = match
        self._offset = offset

    def group(self, group_num=0):
        return self._match.group(group_num)

    def start(self, group_num=0):
        return self._match.start(group_num) + self._offset

    def end(self, group_num=0):
        return self._match.end(group_num) + self._offset

    def span(self, group_num=0):
        return self.start(group_num), self.end(group_num)

def custom_finditer(pattern, text, flags=0):
    """
    Własna implementacja re.finditer.
    :param pattern: Wyrażenie regularne (regex).
    :param text: Tekst do przeszukania.
    :param flags: Flagi (opcjonalne).
    :return: Iterator obiektów CustomMatch.
    """
    pos = 0  # Bieżąca pozycja w tekście
    while pos < len(text):
        match = re.search(pattern, text[pos:], flags)  # Szukaj od bieżącej pozycji
        if not match:
            break  # Jeśli brak dopasowania, przerwij pętlę
        yield CustomMatch(match, offset=pos)
        pos += match.end()  # Przesuń wskaźnik za ostatnie dopasowanie

# Testowanie custom_finditer
pattern = r'\d+'
text = "Liczby 42 i 123 są w tekście."

matches = custom_finditer(pattern, text)
for match in matches:
    print(f"Dopasowanie: {match.group()}, Start: {match.start()}, Koniec: {match.end()}")
# Dopasowanie: 42, Start: 7, Koniec: 9
# Dopasowanie: 123, Start: 12, Koniec: 15