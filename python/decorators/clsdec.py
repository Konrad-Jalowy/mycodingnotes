def add_method(cls):
    cls.new_method = lambda self: "Nowa metoda"
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())