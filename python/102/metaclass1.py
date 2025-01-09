# Metaklasa, która modyfikuje nazwę klasy
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        name = f"Custom{name}"  # Zmiana nazwy klasy
        return super().__new__(cls, name, bases, dct)


# Użycie metaklasy
class MyClass(metaclass=MyMeta):
    pass


print(MyClass.__name__)  # Wynik: CustomMyClass