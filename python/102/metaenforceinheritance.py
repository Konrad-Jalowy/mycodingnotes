class BaseClass:
    def base_method(self):
        return "Method from BaseClass"


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Dodajemy `BaseClass` do bazowych klas, jeśli nie ma jej w `bases`
        if BaseClass not in bases:
            bases = (BaseClass,) + bases
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


obj = MyClass()
print(obj.base_method())  # Wyjście: Method from BaseClass
