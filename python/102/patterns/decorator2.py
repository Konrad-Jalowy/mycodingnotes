from abc import ABC, abstractmethod

# Interfejs bazowy
class Komponent(ABC):
    @abstractmethod
    def rysuj(self) -> str:
        pass

# Podstawowy komponent: Okno
class Okno(Komponent):
    def rysuj(self) -> str:
        return "Rysuję okno"

# Dekorator bazowy
class Dekorator(Komponent):
    def __init__(self, komponent: Komponent):
        self._komponent = komponent

    def rysuj(self) -> str:
        return self._komponent.rysuj()

# Konkretny dekorator: Pasek przewijania
class PasekPrzewijania(Dekorator):
    def rysuj(self) -> str:
        return f"{self._komponent.rysuj()} z paskiem przewijania"

# Konkretny dekorator: Ramka
class Ramka(Dekorator):
    def rysuj(self) -> str:
        return f"{self._komponent.rysuj()} z ramką"

# Konkretny dekorator: Cień
class Cien(Dekorator):
    def rysuj(self) -> str:
        return f"{self._komponent.rysuj()} z cieniem"

# Program
def main():
    # Podstawowe okno
    okno = Okno()
    print(okno.rysuj())

    # Okno z paskiem przewijania
    okno_z_paskiem = PasekPrzewijania(okno)
    print(okno_z_paskiem.rysuj())

    # Okno z paskiem przewijania i ramką
    okno_z_paskiem_i_ramka = Ramka(okno_z_paskiem)
    print(okno_z_paskiem_i_ramka.rysuj())

    # Okno z wszystkimi dekoracjami
    pelne_okno = Cien(okno_z_paskiem_i_ramka)
    print(pelne_okno.rysuj())

if __name__ == "__main__":
    main()