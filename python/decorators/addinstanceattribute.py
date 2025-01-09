def add_instance_attribute(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)  # Wywołanie oryginalnego konstruktora
        self.instance_attribute = "Atrybut instancji"

    cls.__init__ = new_init
    return cls


@add_instance_attribute
class MyClass:
    def __init__(self, name):
        self.name = name


obj = MyClass("Test")
print(obj.name)  # Wyjście: Test
print(obj.instance_attribute)  # Wyjście: Atrybut instancji