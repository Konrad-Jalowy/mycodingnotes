def add_attribute(cls):
    cls.new_attribute = "Dodano nowy atrybut!"
    return cls

@add_attribute
class MyClass:
    pass

print(MyClass.new_attribute)  # Wyjście: Dodano nowy atrybut!