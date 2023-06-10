# random number
import random
print("random number:")
a = random.random()
print(a)

# random number with range
print("random number with range:")
a = random.uniform(1, 10)
print(a)
a = random.uniform(9, 10)
print(a)

# random number with randint
print("random number with randint:")
a = random.randint(1, 10)
print(a)
a = random.randint(7, 10)
print(a)

# random number with randrange
print("random number with randrange:")
a = random.randrange(1, 10)
print(a)
a = random.randrange(7, 10)
print(a)

# random number with normalvarite
print("random number with normalvarite:")
a = random.normalvariate(0, 1)
print(a)

# random chice
print("random choice:")
mylist = list("ABCDEF")
a = random.choice(mylist)
print(mylist)
print(a)

# random sample with element
print("random sample with element:")
mylist = list("ABCDEF")
a = random.sample(mylist, 3)
print(mylist)
print(a)

# random sample with multiple element
print("random sample with multiple element:")
mylist = list("ABCDEF")
a = random.sample(mylist, k=3)
print(mylist)
print(a)

# random sample with shuffle element
print("random sample with shuffle element:")
mylist = list("ABCDEF")
a = random.shuffle(mylist)
print(mylist)

# using random seed
print("using random seed:")
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

print("using random seed:")
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets
# secrets number
print("secrets number:")
a = secrets.randbelow(10)
print(a)

# using randbits function
print("using randbites function:")
a = secrets.randbits(4)
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

# using numpy library with rand function
print("using numpy library with rand function:")
import numpy as np
a = np.random.rand(3)
print(a)

import numpy as np
a = np.random.rand(3, 3)
print(a)

# using numpy library with randint function
print("using numpy library with randint function:")
import numpy as np
a = np.random.randint(0, 10, 3)
print(a)

# using numpy library with multi dimention array
print("using numpy library with multi dimention array:")
import numpy as np
a = np.random.randint(0, 10, (3, 4))
print(a)

# using numpy library with shuffle function
print("using numpy library with shuffle function:")
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
np.random.shuffle(a)
print(a)

# using numpy library with seed function
print("using numpy library with seed function:")
import numpy as np
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
