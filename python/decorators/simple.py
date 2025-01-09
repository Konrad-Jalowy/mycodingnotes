def simple_decorator(func):
    def wrapper():
        print("Przed wykonaniem funkcji")
        func()
        print("Po wykonaniu funkcji")
    return wrapper

@simple_decorator
def my_function():
    print("Jestem w środku funkcji")

my_function()