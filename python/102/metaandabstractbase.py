class AbstractBase:
    def required_method(self):
        raise NotImplementedError("You must implement this method!")


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Sprawdzamy, czy wszystkie metody bazowych klas są zaimplementowane
        for base in bases:
            for attr in dir(base):
                # Pomijamy wbudowane atrybuty/metody zaczynające się od '__'
                if not attr.startswith('__'):
                    base_attr = getattr(base, attr)
                    # Sprawdzamy tylko metody bazowej klasy
                    if callable(base_attr) and attr not in dct:
                        raise TypeError(f"Klasa {name} nie implementuje metody '{attr}' z klasy bazowej {base.__name__}")
        return super().__new__(cls, name, bases, dct)


class MyClass(AbstractBase, metaclass=MyMeta):
    pass


obj = MyClass()