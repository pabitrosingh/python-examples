
# 1. List -> allows duplicates , mutable []
# 2. Tuple -> allows duplicates,  immutable () 
# 3. Set -> no duplicates , {}
# 4. Dictionary -> Key and Value pair (Key shuold be unique)


fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop(2)
for x in fruits:
    print(x)

