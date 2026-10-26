# Semicolons are optional in Python. You can write multiple statements on one line by separating them with
# Text in Python must be inside quotes. You can use either " double quotes or ' single quotes
print("Hello"); print("How are you?"); print("Bye bye!")

#without semicolons it will error out
# print("Python is fun!") print("Really!")

first_name="pabitro"
last_name="singh"
print(first_name,last_name)
print(first_name+last_name)
print(first_name+" "+last_name)
print(f"{first_name}{last_name}")
print(f"{first_name}\t{last_name}")
print(f"{first_name}\n{last_name}")
print("I am", 35, "years old.")

#If you want to print multiple words on the same line, you can use the end parameter
print("Hello World!", end=" ")
print("I will print on the same line.")

print(5)
print(5,5)
print(5,5,5)
print(5+5)
print(5*5)
print(5*5, 5+5)

producd_id = 12345
product_name ="Apple"
mrp=350
print(producd_id,product_name)
print(f"Product ID: {producd_id}\t Name:{product_name}")
print(str(producd_id) + " " + product_name) # using str to cast a number to string 
print(f"{mrp:.2f}") # using :.2f to format the numbers 

"""
This is a comment
written in
more than just one line
"""
