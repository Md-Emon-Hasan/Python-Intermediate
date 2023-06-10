# collection: Counter, namedtuple, OrderedDict, deque
from collections import Counter, defaultdict, namedtuple
# count the data
print("count the data types:")
a = "aaaaabbbbccc"
mycounter = Counter(a)
print(mycounter)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(2))
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements()))

# using multiple variable values
print("using multiple variable values:")
Point = namedtuple('Point','x,y')
pt = Point(1, -4)
print(pt)

point = ('x,y')
pt = Point(1, -4)
print(pt)

from collections import OrderedDict

# order dectionaries
print("order dictionaries:")
orderdict = OrderedDict()
orderdict['a'] = 1
orderdict['b'] = 2
orderdict['c'] = 3
orderdict['d'] = 4
orderdict['e'] = 5
print(orderdict)

orderdict = OrderedDict()
orderdict['b'] = 2
orderdict['c'] = 3
orderdict['d'] = 4
orderdict['e'] = 5
orderdict['a'] = 1
print(orderdict)

# default directories
print("default directories:")
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

from collections import deque

# using deque function
print("using deque function:")
d = deque()
d.append(1)
d.append(2)
print(d)

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

# using deque with pop function
print("using deque with pop function:")
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.pop()
print(d)

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.popleft()
print(d)

# using clear function
print("using clear function:")
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.clear()
print(d)

# using extend function
print("using extende function:")
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.extend([4, 5, 6])
print(d)

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.extendleft([4, 5, 6])
print(d)

# rotate function
print("use rotate function:")
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.extend([4, 5, 6])
d.rotate(1)
print(d)

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.extend([4, 5, 6])
d.rotate(2)
print(d)

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.extend([4, 5, 6])
d.rotate(-1)
print(d)
