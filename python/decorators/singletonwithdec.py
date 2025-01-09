def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    def __init__(self, value):
        self.value = value


obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1 is obj2)  # Wyjście: True
print(obj1.value)  # Wyjście: 10