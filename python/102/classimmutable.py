class Immutable:
    def __new__(cls, value):
        instance = super().__new__(cls)
        instance._value = value
        return instance

    def __setattr__(self, key, value):
        raise AttributeError("Obiekt jest niemutowalny!")

obj = Immutable(10)
print(obj._value)
obj._value = 20  # Podnosi wyjątek AttributeError