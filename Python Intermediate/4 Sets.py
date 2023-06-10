# sets: unordered, mutable, no duplicates
from tkinter import PIESLICE

print("set:")
myset = {1, 2, 3, 4, 5, 6}
print(myset)

myset = {1, 2, 3, 1, 2, 4}
print(myset)

myset = set("hello")
print(myset)

# empty set
print("empty set:")
myset = {}
print(myset)

myset = {}
print(type(myset))

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.discard(3)
print(myset)

# use pop function
print("using pop function:")
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.pop()
print(myset)

# using for loop
print("using pop loop:")
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
for x in myset:
    print(x)
    
# if statement
print("using if statement:")
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
if 3 in myset:
    print("Yes")
    
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
if 4 in myset:
    print("No")

# using unions function
print("using union function:")
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
prims = {2, 3, 5, 7, 11}
unions = odds.union(evens)
print(unions)

# using intersetion functions
print("using intersection function:")
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
prims = {2, 3, 5, 7, 11}
intersections = odds.intersection(evens)
print(intersections)
intersections = odds.intersection(prims)
print(intersections)

# using difference function
print("using difference function:")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
difference = setA.difference(setB)
print(difference)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
difference = setB.difference(setA)
print(difference)

# using symmetric difference function
print("using symmetric difference function:")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
symmetric_difference = setA.symmetric_difference(setB)
print(symmetric_difference)

# using update function
print("using update function:")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
update = setA.update(setB)
print(update)

# using intersection update function
print("using intersection update function:")
setA = {1, 2, 3, 4, 6, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

# using difference update function
print("using difference update function:")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setB.difference_update(setA)
print(setB)

# using symmetric difference update
print("using symmetric difference update:")
setA = {1, 2, 3, 4, 6, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)

# using issubset function
print("using issubset function:")
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA))

# using issuperser function
print("using issuper function:")
setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 2, 3, 4, 5, 6, 7}
print(setB.issuperset(setA))

setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 2, 3, 4, 5, 6, 7, 8}
print(setB.issuperset(setA))

# using isdisjoint section
print("using isdisjoint function:")
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.isdisjoint(setB))

setA = {1, 2, 3, 4, 5, 6}
setC = {7, 8}
print(setA.isdisjoint(setC))

# using copy function
print("using copy function:")
setA = {1, 2, 3, 4, 5, 6}
setB = setA
print(setB)

setA = {1, 2, 3, 4, 5, 6}
setB = setA
setB.add(7)
print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()
setB.add(7)
print(setB)
print(setA)

# using frozen set function
print("using frozen function")
frozen = frozenset([1, 2, 3, 4])
print(frozen)
