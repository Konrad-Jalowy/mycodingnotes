class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(id(s1), id(s2))