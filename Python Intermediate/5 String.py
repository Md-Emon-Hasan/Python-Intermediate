# String: ordered, immatuable, text representation
# creating string
import string
from time import time
from tracemalloc import start


print("create string:")
mystring = "hello world"
print(mystring)

mystring ='hello world'
print(mystring)

# print multiline string
print("multiline string:")
mystring = """hello
world"""
print(mystring)

mystring = """hello \
world"""
print(mystring)

# using index function
print("using index function:")
mystring = "hello world"
mystring1 = mystring[0]
print(mystring1)
mystring1 = mystring[-2]
print(mystring1)
mystring1 = mystring[-1]
print(mystring1)

# using substring function
print("using substring function:")
mystring = "hello world"
mystring1 = mystring[1:5]
print(mystring1)
mystring1 = mystring[::2]
print(mystring1)

# concatenate string
print("concatenet string:")
mystring1 = "hello"
mystring2 = "world"
mystring3 = mystring1 + " " + mystring2
print(mystring3)

# using for loop
print("using for loop:")
mystring1 = "hello"
for i in mystring1:
    print(i)
    
# using if statement
print("using if statement:")
mystring1 = "hello"
if 'h' in mystring1:
    print("yes")
else:
    print("no")

# using strip function for remove white space
print("using strip function for remove white space:")
mystring = "      hello world     "
mystring1 = mystring.strip()
print(mystring1)

# using startswitch function
print("using startswitch function:")
mystring = "hello world"
print(mystring.startswith("hello"))
print(mystring.startswith("world"))

# using endswith function
print("using endswith function:")
mystring = "hello world"
print(mystring.endswith("hello"))
print(mystring.endswith("world"))

# using find function
print("using find function:")
mystring = "hello world"
mystring1 = mystring.find("o")
print(mystring1)
mystring1 = mystring.find("pp")
print(mystring1)

# using count function
print("using count function:")
mystring = "hello world"
mystring1 = mystring.count("o")
print(mystring1)

# using replace function
print("using replace function:")
mystring = "hello world"
mystring1 = mystring.replace("world", "universe")
print(mystring1)

# using split function
print("using split function:")
mystring = "how are you doing"
mystring1 = mystring.split()
print(mystring1)

# using join function
print("using join function:")
mystring = "how are you doing"
mystring1 = ''.join(mystring)
print(mystring1)

# creating multiple list
print("creating multiple list:")
mystring = ["a"] * 6
print(mystring)

# using for loop
# wrong method
print("using for loop:")
mystring = ["a"] * 6
print(mystring)
mystring1 = " "
for i in mystring:
    mystring1 += i
print(mystring1)

# using join function
# right method
print("using join function:")
mystring = ["a"] * 6
print(mystring)
mystring1 = "".join(mystring)
print(mystring1)

from timeit import default_timer as timer
# using for loop
# wrong method
print("using for loop:")
mystring = ["a"] * 6
print(mystring)
start = timer()
mystring1 = " "
for i in mystring:
    mystring1 += i
stop = timer()
print(mystring1)
print(stop - start)

# using join function
# right method
print("using join function:")
mystring = ["a"] * 6
print(mystring)
start = timer()
mystring1 = "".join(mystring)
stop = timer()
print(mystring1)
print(stop - start)

# use % function
print("use percent function:")
var = "Tom"
mystring = "the variable is %s" % var
print(mystring)

var = 3
mystring = "the variable is %d" % var
print(mystring)

var = 3.1416
mystring = "the variable is %f" % var
print(mystring)

var = 3.1416
mystring = "the variable is %.2f" % var
print(mystring)

# use format method
print("use format method:")
var = 3.1416
mystring = "the variable is {}" .format(var)
print(mystring)

var = 3.1416
var1 = "circle"
mystring = "the variable is {} and {}" .format(var,var1)
print(mystring)

# use f-string method
print("use f-string method:")
var = 3.1416
var1 = "circle"
mystring = f"the variable is {var} and {var1}"
print(mystring)

var = 3.1416
var1 = "circle"
mystring = f"the variable is {var * 2} and {var1}"
print(mystring)
