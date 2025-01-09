class MyClass:
    _instance_count = 0  # Pole statyczne

    def __init__(self):
        MyClass._instance_count += 1

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

# Tworzenie obiektów
obj1 = MyClass()
obj2 = MyClass()

# Wywołanie metody klasy
print(MyClass.get_instance_count())  # Wyjście: 2

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Użycie metod statycznych
print(Calculator.add(5, 3))       # Wyjście: 8
print(Calculator.subtract(10, 4))  # Wyjście: 6