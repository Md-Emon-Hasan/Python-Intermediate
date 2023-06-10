# JSON
import json
from pickle import DICT
from unicodedata import name
# encoding
print("encoding:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person)
print(person)
print(personJSON)

import json
# encoding with indent
print("encoding with indent:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4)
print(person)
print(personJSON)

import json
# encoding with indent & separetors
print("encoding with indent & separetors:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4, separators=(';','='))
print(person)
print(personJSON)

import json
# encoding with creating JSON file
print("encoding with creating JSON flle:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4, separators=(';','='))
print(person)
print(personJSON)
with open("person.json", 'w') as file:
    json.dump(person, file)

import json
# encoding with creating JSON file & indent
print("encoding with creating JSON flle & indent:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4, separators=(';','='))
print(person)
print(personJSON)
with open("person.json", 'w') as file:
    json.dump(person, file, indent=4)

# convert from a case string
print("convert from a case string:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
person = json.loads(personJSON)
print(person)

# convert encode to decode
print("convert encode to decode:")
person ={"name": "john", "age": 30, "city": "new york", "hasChildren": False, "titles": ["enginner", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)
    
# encode custom object with default arguments
print("encode custom object with default arguments:")
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encode_user(o):
    if isinstance(o, User):
        return{"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of the type user is not JSON serializable")
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# encode custom object with default arguments
print("encode custom object with default arguments:")
print("another method")
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encode_user(o):
    if isinstance(o, User):
        return{"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of the type user is not JSON serializable")
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user)
print(userJSON)

# decode custom object with default arguments
print("decode custom object with default arguments:")
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encode_user(o):
    if isinstance(o, User):
        return{"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of the type user is not JSON serializable")
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user)
print(userJSON)
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict["name"], age=dict["age"])
    return dict
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
