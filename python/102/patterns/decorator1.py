from abc import ABC, abstractmethod

# Interfejs bazowy
class INapoj(ABC):
    @abstractmethod
    def pobierz_opis(self) -> str:
        pass

    @abstractmethod
    def pobierz_koszt(self) -> float:
        pass


# Konkretny komponent
class Kawa(INapoj):
    def pobierz_opis(self) -> str:
        return "Kawa"

    def pobierz_koszt(self) -> float:
        return 5.00


# Dekorator bazowy
class NapojDekorator(INapoj):
    def __init__(self, napoj: INapoj):
        self._napoj = napoj

    def pobierz_opis(self) -> str:
        return self._napoj.pobierz_opis()

    def pobierz_koszt(self) -> float:
        return self._napoj.pobierz_koszt()


# Konkretny dekorator: Mleko
class Mleko(NapojDekorator):
    def pobierz_opis(self) -> str:
        return f"{self._napoj.pobierz_opis()}, Mleko"

    def pobierz_koszt(self) -> float:
        return self._napoj.pobierz_koszt() + 1.50


# Konkretny dekorator: Cukier
class Cukier(NapojDekorator):
    def pobierz_opis(self) -> str:
        return f"{self._napoj.pobierz_opis()}, Cukier"

    def pobierz_koszt(self) -> float:
        return self._napoj.pobierz_koszt() + 0.50


# Program
def main():
    kawa = Kawa()
    print(f"{kawa.pobierz_opis()} - {kawa.pobierz_koszt()} zł")

    kawa = Mleko(kawa)
    print(f"{kawa.pobierz_opis()} - {kawa.pobierz_koszt()} zł")

    kawa = Cukier(kawa)
    print(f"{kawa.pobierz_opis()} - {kawa.pobierz_koszt()} zł")


if __name__ == "__main__":
    main()