# multipication
print("multipication:")
result = 5 * 7
print(result)

# square
print("square:")
result = 2 ** 4
print(result)

# create multiple list
print("create multiple list:")
zeros = [0] * 10
print(zeros)

zeros = [0, 1] * 10
print(zeros)

# create multiple tuples
print("create multiple tuples:")
zeros = (0, 1) * 10
print(zeros)

# create multiple string
print("create multiple string:")
zeros = "ABC" * 10
print(zeros)

# function with args and kwargs
print("function with args and kwargs:")
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1, 2, 3, 4, 5, six = 6, seven = 7)

# function with asterlick value
print("function with asterlick value:")
def foo(a, b, *, c):
    print(a, b, c)
foo(1, 2, c=3)

# function with list
print("function with list:")
def foo(a, b, c):
    print(a, b, c)
my_list = [0, 1, 2]
foo(*my_list)

# function with tuple
print("function with tuple:")
def foo(a, b, c):
    print(a, b, c)
my_list = [0, 1, 2]
foo(*my_list)

# function with my dict
print("function with my dict:")
def foo (a, b, c):
    print(a, b, c)
my_dict = {"a":1, "b":2, "c":3}
foo(**my_dict)

# its show the last number
print("its show the last number:")
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last =  numbers
print(beginning)
print(last)

numbers = (1, 2, 3, 4, 5, 6)
*beginning, last = numbers
print(beginning)
print(last)

# its show the middle and last element
print("its show the middle and last element:")
numbers = (1, 2, 3, 4, 5, 6)
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

# its show the middle, secondlast and last element
print("its show the middle, secondlast and last element:")
numbers = (1, 2, 3, 4, 5, 6)
beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)

# touple and list addition
print("touple and list addition:")
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list = [*my_tuple, *my_list]
print(new_list)

# touple and other addition
print("touple and other addition:")
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
new_list = [*my_tuple, *my_set]
print(new_list)

dict_a = {"a":1, "b":2}
dict_b = {"c":3, "d":4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
