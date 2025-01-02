def starDecorator(func):
    def wrap_func(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
        print("************")
    return wrap_func

@starDecorator
def say_hello(name):
    print("hello " + name)

say_hello("john")
say_hello("jane")