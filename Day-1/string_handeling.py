b = "Hello, World!"
print(b[2:5]) #Slicing

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

txt = "For only {price:.2f} dollars!" #Placeholders and Modifiers using format method
print(txt.format(price = 49))

#All string methods return new values. They do not change the original string
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print("I love apples, apple are my favorite fruit","applie occures :",x, "times")

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(3)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome") #index()
print("Hello, welcome to my world.","welcome is found at positino:",x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P") #replace
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "50"
x = txt.zfill(10) #Fill the string with zeros until it is 10 characters long
print(x)