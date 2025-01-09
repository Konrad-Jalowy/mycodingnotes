class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Jeśli klasa nie ma atrybutu `default_attr`, dodajemy go
        if "default_attr" not in dct:
            dct["default_attr"] = "Default Value"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


print(MyClass.default_attr)  # Wyjście: Default Value