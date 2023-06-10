# decorator
print("decorator:")
def start_and_decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
def print_name():
    print("alex")
print_name = start_and_decorator(print_name)
print_name()

# with @ method
print("with @ method:")
def start_end_decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
@start_end_decorator
def print_name():
    print("alex")

# with value add function
print("with value add function")
def start_and_decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper
@start_and_decorator
def add5(x):
    return x + 5
result = add5(10)
print(result)

# with identify function
print("with identify function:")
# def start_and_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper
# @start_and_decorator
# def add5(x):
#     return x + 5
# print(help(result))
# print(add5.__name__)

# with identify function
print("with identify function:")
# import functools
# def try_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do...
#         result = func(*args, **kwargs)
#         # Do...
#         return result
#     return wrapper
# @start_and_decorator
# def add5(x):
#     return x + 5
# print(help(result))

# simple decorators
print("simple decorators:")
import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times = 3)
def greet(name):
    print(f'Hello {name}')
greet("Alex")

# nested decorators
print("nested decorators:")
import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r}returned {result!r}")
        return result
    return wrapper
@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello{name}'
    print(greeting)
    return greeting
say_hello("alex")

# function decorator
print("function decorator:")
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        print("Hi there")
cc = CountCalls(None)
cc()
@CountCalls
def say_hello():
    print("hello")

# function decorator
print("function decorator:")
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Hi there{self.num_calls} times")
        return self.func(*args, **kwargs)
@CountCalls
def say_hello():
    print("hello")
say_hello()

# function decorator
print("function decorator:")
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Hi there{self.num_calls} times")
        return self.func(*args, **kwargs)
@CountCalls
def say_hello():
    print("hello")
say_hello()
say_hello()

