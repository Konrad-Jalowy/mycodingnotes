def modify_method(cls):
    original_method = cls.method

    def new_method(self, *args, **kwargs):
        print("Przed oryginalną metodą")
        result = original_method(self, *args, **kwargs)
        print("Po oryginalnej metodzie")
        return result

    cls.method = new_method
    return cls


@modify_method
class MyClass:
    def method(self):
        print("Oryginalna metoda!")


obj = MyClass()
obj.method()
# Wyjście:
# Przed oryginalną metodą
# Oryginalna metoda!
# Po oryginalnej metodzie