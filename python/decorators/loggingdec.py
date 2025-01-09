def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func.__name__} z argumentami {args} i {kwargs}")
        result = func(*args, **kwargs)
        print(f"Zwrócono wartość: {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(3, 5)