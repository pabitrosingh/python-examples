v1=int(input("Enter a Number"))
v2=int(input("Enter a Number"))
v3=int(input("Enter a Number"))

if v1 > v2 and v1 > v3:
    print(f"{v1} is bigger than {v2} and {v3}")
elif v2 > v3:
    print(f"{v2} is bigger than {v1} and {v3}")
else: 
    print(f"{v3} is bigger than {v1} and {v2}")

print("------Conditional Statements----")
a = 33
b = 200
if b > a:
  print("b is greater than a")

print("---------------")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("--------------")
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

print("-------------")
'''
The else keyword catches anything which isn't caught by the preceding conditions.
The else statement is executed when the if condition (and any elif conditions) evaluate to False.
You can also have an else without the elif
The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
The else statement must come last. You cannot have an elif after an else
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("--------")

username = input("Enter your name: ")

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
print("--------")

# Short hand if , You still need the colon : after the condition.
a = 5
b = 2
if a > b: print("a is greater than b")

# Short hand if ... else 
# This is called a conditional expression (sometimes known as a "ternary operator").
a = 2
b = 330
print("A") if a > b else print("B")

#You can also use a one-line if/else to choose a value and assign it to a variable
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Logical Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("-----------")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print("--------------")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

print("------------")
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

print("----------")
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

print("------------")
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

#if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error

a = 33
b = 200

if b > a:
  pass



#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.

print("---------------")
day = 4

match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

print("---------------")
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

#You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
