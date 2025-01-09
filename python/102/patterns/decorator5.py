from abc import ABC, abstractmethod

# Interfejs bazowy
class Walidator(ABC):
    @abstractmethod
    def waliduj(self, dane: str) -> bool:
        pass


# Komponent główny
class PodstawowyWalidator(Walidator):
    def waliduj(self, dane: str) -> bool:
        return True  # Zawsze poprawne


# Dekorator bazowy
class WalidatorDekorator(Walidator):
    def __init__(self, walidator: Walidator):
        self._walidator = walidator

    def waliduj(self, dane: str) -> bool:
        return self._walidator.waliduj(dane)


# Konkretny dekorator: Sprawdzenie długości
class DlugoscWalidator(WalidatorDekorator):
    def waliduj(self, dane: str) -> bool:
        return len(dane) > 5 and self._walidator.waliduj(dane)


# Konkretny dekorator: Sprawdzenie cyfr
class CyfryWalidator(WalidatorDekorator):
    def waliduj(self, dane: str) -> bool:
        return any(char.isdigit() for char in dane) and self._walidator.waliduj(dane)


# Program
def main():
    walidator = PodstawowyWalidator()

    # Walidator długości
    walidator_z_dluga_dlugoscia = DlugoscWalidator(walidator)
    print(walidator_z_dluga_dlugoscia.waliduj("krótko"))  # False
    print(walidator_z_dluga_dlugoscia.waliduj("wystarczająco długo"))  # True

    # Walidator długości i cyfr
    walidator_z_dluga_dlugoscia_i_cyframi = CyfryWalidator(walidator_z_dluga_dlugoscia)
    print(walidator_z_dluga_dlugoscia_i_cyframi.waliduj("brakcyfr"))  # False
    print(walidator_z_dluga_dlugoscia_i_cyframi.waliduj("wystarczająco2"))  # True

if __name__ == "__main__":
    main()