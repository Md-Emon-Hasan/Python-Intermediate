# generators
print("generators:")
def mygenarator():
    yield 1
    yield 2
    yield 3
g = mygenarator()
print(g)

# generators
print("generators:")
def mygenarator():
    yield 1
    yield 2
    yield 3
g = mygenarator()
for i in g:
    print(i)
    
# generators
print("generators:")
def mygenarator():
    yield 1
    yield 2
    yield 3
g = mygenarator()
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)

# generators
print("generators:")
def mygenarator():
    yield 1
    yield 2
    yield 3
g = mygenarator()
print(sorted(g))

# generators
print("generators:")
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))

# generators
print("generators:")
def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
print(first(10))

# genarators
print("generators:")
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def first_genarator(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sum(firstn(10)))
print(sum(first_genarator(10)))

# generartor with memory value
print("generartor with memory value:")
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def first_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sys.getsizeof(firstn(10000000)))
print(sys.getsizeof(first_generator(10000000)))

# generator with fibonacci
print("generator with fibonacci:")
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
fib = fibonacci(30)
for i in fib:
    print(i)
    
# generator
print("generator:")
mygenarator = (i for i in range(10) if i % 2 == 0)
for i in mygenarator:
    print(i)
    
# create generator with size
print("create generator with size:")
import sys
mygenarator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof(mygenarator))
mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))

import sys
mygenarator = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(mygenarator))
mylist = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(mylist))
