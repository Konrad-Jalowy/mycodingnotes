class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Dodajemy nową metodę do klasy
        dct["new_method"] = lambda self: "This is a new method!"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


obj = MyClass()
print(obj.new_method())  # Wyjście: This is a new method!
