# function
print("function:")
def print_name(name):
    print(name)
print_name("alex")

# function
print("function:")
def foo(a, b, c):
    print(a, b, c)
foo(1, 2, 3)

# function with value
print("function with value:")
def foo(a, b, c):
    print(a, b, c)
foo(a=1, b=2, c=3)

# function with different value
print("function with different value:")
def foo(a, b, c):
    print(a, b, c)
foo(1, b=2, c=3)

# function with different value
print("function with different value:")
def foo(a, b, c, d = 4):
    print(a, b, c, d)
foo(1, 2, 3)

# function with different value
print("function with different value:")
def foo(a, b, c, d = 4):
    print(a, b, c, d)
foo(1, 2, 3, 7)

# function with different value
print("function with different value:")
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1, 2, 3, 4, 5, six = 6, seven = 7)

# function with different value
print("function with different value:")
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1, 2, 3, 4, 5)

# function
print("function:")
def foo(a, b, *, c, d):
    print(a, b, c, d)
foo(1, 2, c = 3, d = 4)

# function with perameter
print("function with perameter:")
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo(1, 2, 3, last = 300)

# function
print("function:")
def foo(a, b, c):
    print(a, b, c)
my_list = (0, 1, 2)
foo(*my_list)

# function with dictionary
print("function with dictionary:")
def foo(a, b, c):
    print(a, b, c)
my_dict = {"a":1, "b":2, "c":3}
foo(**my_dict)

# function with global variable
print("function with global variable:")
def foo():
    global number
    x = number
    number = 3
    print("number inside function",x)
number = 0
foo()
print(number)

# function with muteable object
print("function with muteable object:")
def foo(a_list):
    a_list.append(4)
my_list = [1, 2, 3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list.append(4)
    a_list[0] = -100
my_list = [1, 2, 3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list += [200, 300, 400]
my_list = [1, 2, 3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list = a_list + [200, 300, 400]
my_list = [1, 2, 3]
foo(my_list)
print(my_list)
