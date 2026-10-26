# apart from int, float 

x = 1j
print(x,type(x))

x = range(6)
print(x,type(x))

x = ["apple", "banana", "cherry"] #list
print(x,type(x))

x = ("apple", "banana", "cherry") #tuple
print(x,type(x))


x = {"name" : "John", "age" : 36} #dict
print(x,type(x))

x = {"apple", "banana", "cherry"} #set
print(x,type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x,type(x))

x=True
print(x,type(x))

x=None
print(x,type(x))

x = b"Hello"
print(x,type(x))

x = bytearray(5)
print(x,type(x))

x = memoryview(bytes(5))
print(x,type(x))

# You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))

# Multiple String 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Like many other popular programming languages, strings in Python are arrays of unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(f"length of Hello, World!={len(a)}")

# To check if a certain phrase or character is present in a string, we can use the keyword in and not in
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)