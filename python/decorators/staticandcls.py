class MyClass:
    @staticmethod
    def static_method():
        print("To jest metoda statyczna")

    @classmethod
    def class_method(cls):
        print(f"To jest metoda klasy {cls.__name__}")

MyClass.static_method()
MyClass.class_method()