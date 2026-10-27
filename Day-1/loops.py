n=int(input("Enter n Value"))
for i in range(n, 0,-1):
    print(i)
    
n=int(input("Enter n Value"))
for i in range(1, n+1,1):
    print(i)

print("-----")
for i in range(5):
  print(i)
print("-----")
r = range(10)
print(r[2])
print(r[:3])

print("-----")
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
print("-----")
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

print("--------")
r = range(0, 10, 2)
print(len(r))

#while loop 
i = 1
while i < 6:
  print(i)
  i += 1 #remember to increment i, or else the loop will continue forever.
print("--------")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("--------")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("--------")
# Loop with else , The else block will NOT be executed if the loop is stopped by a break statement.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("--------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("--------")
for x in "banana":
  print(x)

print("------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("------")
for x in range(6):
  print(x)
else:
  print("Finally finished!") #The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# The else block will NOT be executed if the loop is stopped by a break statement.

print("------------------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
