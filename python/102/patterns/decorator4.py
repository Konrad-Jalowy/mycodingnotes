from abc import ABC, abstractmethod

# Interfejs bazowy
class Plik(ABC):
    @abstractmethod
    def zapisuj(self, dane: str) -> str:
        pass


# Podstawowy komponent
class ZwyklyPlik(Plik):
    def zapisuj(self, dane: str) -> str:
        return f"Zapisano dane: {dane}"


# Dekorator bazowy
class PlikDekorator(Plik):
    def __init__(self, plik: Plik):
        self._plik = plik

    def zapisuj(self, dane: str) -> str:
        return self._plik.zapisuj(dane)


# Dekorator: Szyfrowanie
class Szyfrowanie(PlikDekorator):
    def zapisuj(self, dane: str) -> str:
        zaszyfrowane_dane = ''.join(reversed(dane))  # Proste "szyfrowanie"
        return self._plik.zapisuj(f"[SZYFROWANE] {zaszyfrowane_dane}")


# Dekorator: Kompresja
class Kompresja(PlikDekorator):
    def zapisuj(self, dane: str) -> str:
        skompresowane_dane = dane.replace(" ", "")  # Prosta "kompresja"
        return self._plik.zapisuj(f"[KOMPRESOWANE] {skompresowane_dane}")


# Program
def main():
    plik = ZwyklyPlik()

    # Plik z szyfrowaniem
    plik_szyfrowany = Szyfrowanie(plik)
    print(plik_szyfrowany.zapisuj("To są ważne dane"))

    # Plik z kompresją i szyfrowaniem
    plik_skompresowany_i_szyfrowany = Szyfrowanie(Kompresja(plik))
    print(plik_skompresowany_i_szyfrowany.zapisuj("To są bardzo ważne dane"))

if __name__ == "__main__":
    main()
