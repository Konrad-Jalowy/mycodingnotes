class RequireRunMeta(type):
    def __new__(cls, name, bases, dct):
        if "run" not in dct:
            raise TypeError(f"Klasa {name} musi definiować metodę 'run'")
        return super().__new__(cls, name, bases, dct)


# Klasa używająca metaklasy
class MyClass(metaclass=RequireRunMeta):
    def run(self):
        print("Uruchamiam się!")


class InvalidClass(metaclass=RequireRunMeta):
    pass  # Brak metody 'run', podniesie TypeError