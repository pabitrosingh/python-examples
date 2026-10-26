#Python has no command for declaring a variable.
#Variables do not need to be declared with any particular type, and can even change type after they have been set.
# Variable names are case-sensitive.
# we can use global keyword to declare a global variable

x=10
print(x)
print(type(x))
x=2.50
print(x)
print(type(x))
x="Hello"
print(x)
print(type(x))

#If you want to specify the data type of a variable, this can be done with casting
p = str(3333333)    # x will be '3'
q = int(3333333333)    # y will be 3
r = float(33333.00000)  # z will be 3.0
print(p)
p="test"
print(p)

# Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)