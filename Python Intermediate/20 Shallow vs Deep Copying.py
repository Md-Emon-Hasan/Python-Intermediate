# default copy
print("default copy:")
org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

# default copy
print("default copy:")
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

# shallow copy
print("shallow copy:")
import copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

# shallow copy
print("shallow copy:")
import copy
org = [0, 1, 2, 3, 4]
cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

# shallow copy
print("shallow copy:")
import copy
org = [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]
cpy = copy.copy(org)
cpy[0][1] = - 10
print(cpy)
print(org)

# deep copy
print("deep copy:")
import copy
org = [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

# inheritence
print("inheritence:")
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Alex", 27)
p2 = copy.copy(p1)
p2.age = 28
print(p2.age)
print(p1.age)

# inheritence with shellow copy
print("inheritence with shellow copy:")
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
p1 = Person("Alex", 55)
p2 = Person("joe", 27)
company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company_clone.boss.age)

# inheritence with deep copy
print("inheritence with deep copy:")
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
p1 = Person("Alex", 55)
p2 = Person("joe", 27)
company = Company(p1, p2)
company_clone = copy.copydeep(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company_clone.boss.age)