# Error & Exceptions
# x = - 5
# if x < 0:
#     raise Exception("x should be posetive")

# x = 5
# if x < 5:
#     raise Exception("x should be posetive")

# using assertion error
print("assertion error:")
# x = -5
# assert (x >= 0), 'x is not posetive'

# zero divisin error
print("using zero division error:")
# a = 5 / 0

# using try except error
print("using try except:")
try:
    a = 5 / 0
except:
    print("an error detected")
    
# using try except error with massage
print("using try except with massage:")
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# using multiple exception
print("using multiple exception:")
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print("using try except with else:")
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")

print("using try except with else & finally:")
try:
    a = 5 / 0
    b = a + 10
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("everythin is fine")
finally:
    print("cleaning up...")

print("using try except with else & finally:")
try:
    a = 5 / 0
    b = a + 10
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("everythin is fine")
finally:
    print("cleaning up...")

try:
    a = 5 / 1
    b = a + 10
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("everythin is fine")
finally:
    print("cleaning up...")
    
# value check
# print("check the value:")    
# class ValueTooHighError(Exception):
#     pass
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError("value is too high")
# test_value(101)

# class ValueTooHighError(Exception):
#     pass
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError("value is too high")
# try:
#     test_value(200)
# except ValueTooHighError as e:
#     print(e)

class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 100:
        raise ValueTooSmallError("value is too small", x)
try:
    test_value(20)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
