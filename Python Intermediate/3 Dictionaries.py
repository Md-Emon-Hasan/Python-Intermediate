# Dctionaries: Key-Value paris, Unordered, Mutable
from msilib import PID_TITLE
from unicodedata import name

# creating dictionaries
print("creating dictionaries:")
mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

mydict1 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict1)

mydict1 = dict(name = "Mary", age = 27, city = "Boston")
value = mydict["age"]
print(value)

mydict1 = dict(name = "Mary", age = 27, city = "Boston")
value = mydict["city"]
print(value)

mydict = dict(name = "Mary", age = 27, city = "Boston")
print(mydict)
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# for remove value
print("for remove values:")
mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)
del mydict["name"]
print(mydict)

# for remove value
mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)
mydict.pop("age")
print(mydict)

# for remove value
mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)
mydict.popitem()
print(mydict)

# using if statement
print("using if statement:")
mydict = {"name":"Max", "age":28, "city":"New York"}
if "name" in mydict:
    print(mydict["name"])

# using try catch statement
print("using try catch statement:")
mydict = {"name":"Max", "age":28, "city":"New York"}
try:
    print(mydict["lastname"])
except:
    print("error")

# using for loop
print("using for loop:")
mydict = {"name":"Max", "age":28, "city":"New York"}
for key in mydict:
    print(key)
    
mydict = {"name":"Max", "age":28, "city":"New York"}
for key in mydict.values():
    print(key)
    
# using copy
print("using copy function:")
mydict = {"name":"Max", "age":28, "city":"New York"}
mydict1 =  mydict
print(mydict1)

mydict = {"name":"Max", "age":28, "city":"New York"}
mydict1 = mydict
mydict1["email"] = "max@xyz.com"
print(mydict1)
print(mydict)

# actual copy
print("using actual cop function:")
mydict = {"name":"Max", "age":28, "city":"New York"}
mydict1 = mydict.copy()
mydict1["email"] = "max@xyz.com"
print(mydict)
print(mydict1)

mydict = {"name":"Max", "age":28, "city":"New York"}
mydict1 = dict(mydict)
mydict1["email"] = "max@xyz.com"
print(mydict)
print(mydict1)

# update dictionaries
print("using update dictionaries function:")
mydict = {"name":"Max", "age":28, "email":"max@xyz.com"}
mydict1 = dict(name = "Marry", age = 27, city = "Boston")
mydict.update(mydict1)
print(mydict)

# integer data types
print("using integer data types:")
mydict = {3:9, 6:36, 9:81}
print(mydict)

# print with specific value
print("print with specific value:")
mydict = {3:9, 6:36, 9:81}
value = mydict[3]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)
