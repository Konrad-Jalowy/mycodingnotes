from abc import ABC, abstractmethod

# Interfejs bazowy
class Middleware(ABC):
    @abstractmethod
    def przetwarzaj(self, dane: dict) -> str:
        pass

# Komponent główny
class Serwer(Middleware):
    def przetwarzaj(self, dane: dict) -> str:
        return f"Obsługa żądania: {dane.get('ścieżka', '/')}"


# Dekorator bazowy
class MiddlewareDekorator(Middleware):
    def __init__(self, komponent: Middleware):
        self._komponent = komponent

    def przetwarzaj(self, dane: dict) -> str:
        return self._komponent.przetwarzaj(dane)


# Middleware: Logowanie
class Logowanie(MiddlewareDekorator):
    def przetwarzaj(self, dane: dict) -> str:
        print(f"[LOG] Żądanie na ścieżkę: {dane.get('ścieżka', '/')} - Dane: {dane}")
        return self._komponent.przetwarzaj(dane)


# Middleware: Autoryzacja
class Autoryzacja(MiddlewareDekorator):
    def przetwarzaj(self, dane: dict) -> str:
        if not dane.get("autoryzowany", False):
            return "403 Forbidden: Brak dostępu!"
        return self._komponent.przetwarzaj(dane)


# Program
def main():
    serwer = Serwer()

    # Dodanie middleware
    serwer_z_autoryzacja = Autoryzacja(serwer)
    serwer_z_autoryzacja_i_logowaniem = Logowanie(serwer_z_autoryzacja)

    # Żądania
    print(serwer_z_autoryzacja_i_logowaniem.przetwarzaj({"ścieżka": "/home", "autoryzowany": True}))
    print(serwer_z_autoryzacja_i_logowaniem.przetwarzaj({"ścieżka": "/admin", "autoryzowany": False}))

if __name__ == "__main__":
    main()
