def uppercase_decorator(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        return result.upper()
    return wrapper

class Greeter:
    @uppercase_decorator
    def greet(self, name):
        return f"Hello, {name}"

g = Greeter()
print(g.greet("world"))