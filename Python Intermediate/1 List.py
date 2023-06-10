# lists: ordered, mutable, allows duplicate elements
print("list:")
mylist = ["banana", "cherry", "apple"]
print(mylist)

# create empty list
print("empty list:")
mylist = list()
print(mylist)
mylist = []
print(mylist)

# list allow anything
print("allow anything list:")
mylist = [5, True, "apple"]
print(mylist)

# list also allow duplicate eliment
print("allow duplicate element:")
mylist = ["apple", "apple"]
print(mylist)

# print with index value
print("print with index value:")
mylist = ["banana", "cherry", "apple"]
list = mylist[0]
print(list)
list = mylist[-1]
print(list)

# with using for loop
print("using for loop:")
mylist = ["banana", "cherry", "apple"]
for i in mylist:
    print(i)
    
# with if statement
print("with if statement:")
mylist = ["banana", "cherry", "apple"]
if "banana" in mylist:
    print("Yes")
else:
    print("No")
    
mylist = ["banana", "cherry", "apple"]
if "Orange" in mylist:
    print("Yes")
else:
    print("No")
    
# check list length
print("check list length:")
mylist = ["banana", "cherry", "apple"]
mylist1 = len(mylist)
print(mylist1)

mylist = ["banana", "cherry", "apple"]
print(len(mylist))

# append finction
print("using append function:")
mylist = ["banana", "cherry", "apple"]
mylist.append("lemon")
print(mylist)

# insert function
print("using insert function:")
mylist = ["banana", "cherry", "apple"]
mylist.insert(1, "bluebarry")
print(mylist)

# use pop for remove last element
print("use pop for remove last element:")
mylist = ["banana", "cherry", "apple"]
mylist.pop()
print(mylist)

# remove function
print("using remove function:")
mylist = ["banana", "cherry", "apple"]
mylist.remove("cherry")
print(mylist)

# reverse function
print("using reverse function:")
mylist = ["banana", "cherry", "apple"]
mylist.reverse()
print(mylist)

# sort function
print("using sort function:")
mylist = ["banana", "cherry", "apple"]
mylist.sort()
print(mylist)

mylist = [5, 9, 3, 4, -6, -9, -2]
mylist.sort()
print(mylist)

mylist = [5, 9, 3, 4, -6, -9, -2]
newlist = sorted(mylist)
print(newlist)

# multiple list
print("create multiple list:")
mylist = [0] * 5
print(mylist)

# adding list
print("using add function:")
mylist1 = [1, 2, 3, 4, 5]
mylist2 = [6, 7, 8, 9, 10]
mylist = mylist1 + mylist2
print(mylist)

# slicing index
print("using slicing index")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[1:5]
print(a)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[:5]
print(a)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[1:]
print(a)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[::1]
print(a)

# jumping one list
print("jumping one by one list:")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[::2]
print(a)

# reverse list
print("create reverse list:")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[::-1]
print(a)

# list copying
print("using list copy:")
list_original = ["banana", "cherry", "apple"]
list_copy = list_original
print(list_copy)

list_original = ["banana", "cherry", "apple"]
list_copy = list_original.copy()
list_copy.append("lemon")
print(list_copy)
print(list_original)

list_original = ["banana", "cherry", "apple"]
list_copy = list_original[:]
list_copy.append("lemon")
print(list_copy)
print(list_original)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)
