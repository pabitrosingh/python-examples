#The self parameter must be the first parameter of any method in the class
#The self parameter is a reference to the current instance of the class
#All classes have a built-in method called __init__(), which is always executed when the class is being initiated
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
#Properties defined inside __init__() belong to each object (instance properties).
#Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:


class Employee:
    id=int
    name=str

    def printData(self):
        print(self.id,self.name)

emp = Employee()
emp.id = 1
emp.name = "David"
emp.printData()

print("--------------")
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

print("------------------")
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

print("---------------------")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
p1.age = 26
print(p1.age)

print("--------------")
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

print("----------------")
#Methods are functions that belong to a class. They define the behavior of objects created from the class
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

print("-----------")
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
print("--------------")
#The __str__() method is a special method that controls what is returned when the object is printed
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)
print("----------------")
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
print("--------------------")

"""
Magic methods are special methods whose names start and end with double underscores, 
like __init__() and __str__(). Because of the double underscores,
 they are also called dunder methods (short for "double underscore").
"""

