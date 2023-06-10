# tuples: ordered, immuatable, allows duplicate element
from types import CoroutineType

mytuple = ("max", 28, "Boston")
print(mytuple)

mytuple = ("max")
print(type(mytuple))

mytuple = tuple(["max", 28, "Boston"])
print(mytuple)

# print with index value
print("print with index value:")
mytuple = tuple(["max", 28, "Boston"])
item = mytuple[2]
print(item)

mytuple = ("max", 28, "Boston")
print(mytuple)
for i in mytuple:
    print(i)
    
mytuple = ("max", 28, "Boston")
if "max" in mytuple:
    print("Yes")
else:
    print("No")
    
mytuple = ("max", 28, "Boston")
if "hello" in mytuple:
    print("Yes")
else:
    print("No")
    
# length count
print("using length function:")
mytuple = ('a', 'p', 'p', 'l', 'e')
mytuple1 = len(mytuple)
print(mytuple1)

# for letter counting
print("using counting function:")
mytuple = ('a', 'p', 'p', 'l', 'e')
print(mytuple.count('p'))
print(mytuple.count('l'))
print(mytuple.count("0"))

# find index value
print("finding index value:")
mytuple = ('a', 'p', 'p', 'l', 'e')
print(mytuple.index("e"))

mytuple = ('a', 'p', 'p', 'l', 'e')
mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)
print(mytuple2)

# print with specific value
print("print with specific value:")
mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = mytuple[2:5]
print(b)

mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = mytuple[:1]
print(b)

mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = mytuple[::1]
print(b)

mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = mytuple[1:]
print(b)

mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = mytuple[::-1]
print(b)

mytuple = "Max", 28, "Boston"
name, age, city = mytuple
print(name)
print(age)
print(city)

mytuple = (1, 2, 3, 4, 5, 6)
i1, *i2 , i3 = mytuple
print(i1)
print(i3)
print(i2)
print(*i2)

# showing file size
print("showing file size")
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

# showing execute time
print("showing execute time")
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=100000)) 
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=100000))
 