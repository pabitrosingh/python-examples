#Decorators let you add extra behavior to a function, without changing the function's code
#A decorator is a function that takes another function as input and returns a new function
#Define the decorator first, then apply it with @decorator_name above the function.
#Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function
#Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

print("-----------")
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction(input("enter your name: ")))

print("-----multiple decorators------")
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
