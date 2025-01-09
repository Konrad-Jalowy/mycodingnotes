# classmethod is basically static method from other languages
# and staticmethod is just some util method that can be called by class
class MyClass:
    class_attribute = "Atrybut klasy"

    @classmethod
    def class_method(cls):
        return f"Jestem metodą klasy, mam dostęp do cls: {cls.class_attribute}"

print(MyClass.class_method())