class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Wywołano __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Wywołano __init__")
        self.value = value

obj = MyClass(10)