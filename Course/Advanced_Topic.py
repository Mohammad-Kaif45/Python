# Decorator : A decorator is just a function that modifies another function
# without changing its actual code.


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result
    return wrapper


@decorator
def hello(name):
    print(f"Hello {name}")

hello("World")

# args and kwargs in decorator
# They’re special keywords in Python used in function definitions to
# accept a flexible number of arguments.
# The important part is the * and ** syntax. You can use any name
# in front of them, but *args and **kwargs are the common conventions.
# *args is used for positional arguments and becomes a tuple.
# **kwargs is used for keyword arguments and becomes a dictionary.

# if you can want



