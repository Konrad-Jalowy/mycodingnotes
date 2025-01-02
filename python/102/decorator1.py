def starDecorator(func):
    def wrap_func():
        print("************")
        func()
        print("************")
    return wrap_func

@starDecorator
def say_hello():
    print("hello")

say_hello()