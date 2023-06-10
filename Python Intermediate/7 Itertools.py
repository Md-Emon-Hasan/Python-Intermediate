# Itertools: product, permutations, combinations, accumulate, groupby, and infinite itertors
from audioop import mul
from itertools import product
# produc tools
print("product tools:")
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod))

a = [1, 2]
b = [3, 4]
prod = product(a,b, repeat=2)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
# using permutations
print("using permutations:")
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

# with different ordering
print("with differnt order:")
a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

from itertools import combinations
# using combinations
print("using combinations:")
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations, combinations_with_replacement
# using combination with replacement
print("using combination with replacement:")
a = [1, 2, 3, 4]
comb = combinations_with_replacement(a, 2)
print(list(comb))

from itertools import accumulate
# using accumulate function
print("using accumulate:")
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import accumulate
import operator
# using accumulate with operator function
print("using accumulate with operator function:")
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.add)
print(a)
print(list(acc))

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.sub)
print(a)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

from itertools import groupby
# using groupby function
print("using groupby function:")
def smallerThen3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smallerThen3)
for key, value in group_obj:
    print(key, list(value))
    
def smallerThen3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))
    
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
    
from itertools import count, cycle, repeat
# using count, cycle and repeat
print("using count, cycle and repeat function:")
# using count method
# for i in count(10):
#     print(i)

for i in count(10):
    print(i)
    if i == 15:
        break

# uisng cycle method
# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)
    
# using repeat function
# a = [1, 2, 3]
# for i in repeat(1):
#     print(i)
