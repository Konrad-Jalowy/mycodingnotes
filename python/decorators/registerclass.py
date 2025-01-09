class_registry = []

def register_class(cls):
    class_registry.append(cls)
    return cls

@register_class
class MyClass1:
    pass

@register_class
class MyClass2:
    pass

print(class_registry)  
# Wyjście: [<class '__main__.MyClass1'>, <class '__main__.MyClass2'>]