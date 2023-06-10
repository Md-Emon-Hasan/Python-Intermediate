# lambda arguments: expression
# print lambda functiob
from itertools import product

print("uisng lambda function:")
add10 = lambda x: x + 10
print(add10(5))

mul = lambda x,y: x + y
print(mul(2,3))

mul = lambda x,y: x * y 
print(mul(5,7))

# using sorted list
print("using sorted function:")
point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_shorted = sorted(point2D)
print(point2D)
print(point2D_shorted)

# shorted with y index
print("shorted with y index")
point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_shorted = sorted(point2D, key=lambda x: x[1])
print(point2D)
print(point2D_shorted)

point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_shorted = sorted(point2D, key=lambda x: x[0] + x[1])
print(point2D)
print(point2D_shorted)

# using map(func, seq) function
print("using map(func, sequence):")
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(a))
print(list(b))

# second method
a = [1, 2, 3, 4]
c = [x * 2 for x in a]
print(a)
print(list(c))

# using filter(func, seq) function
print("using filter(func, seq) function:")
a = [1, 2, 3, 4]
b = map(lambda x: x % 2 == 0, a)
print(list(b))

a = [1, 2, 3, 4]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# second method
a = [1, 2, 3, 4]
c = [x for x in a if x % 2 == 0]
print(list(c))

from functools import reduce
# using reduce(func, seq) function
print("using reduce(func, seq) function:")
a = [1, 2, 3, 4]
b = reduce(lambda x,y: x * y, a)
print(b)

a = [1, 2, 3, 4]
b = reduce(lambda x,y: x + y, a)
print(b)
