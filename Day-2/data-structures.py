
# 1. List -> allows duplicates , mutable []
# 2. Tuple -> allows duplicates,  immutable () 
# 3. Set -> no duplicates , {}
# 4. Dictionary -> Key and Value pair (Key shuold be unique)


#List
#Lists are used to store multiple items in a single variable
#Lists are created using square brackets
#List items are ordered, changeable, and allow duplicate values
#List items are indexed, the first item has index [0], the second item has index [1] etc
#If you add new items to a list, the new items will be placed at the end of the lis
#List items can be of any data type and it can contain different data types combination
#The first item has index 0,Negative indexing means start from the end,-1 refers to the last item, -2 refers to the second last item etc.
#The length of the list will change when the number of items inserted does not match the number of items replaced.
"""
Method	    Description
----------------------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop(2)
for x in fruits:
    print(x)

print("------------")
list1 = ["abc", 34, True, 40, "male"]
print(list1)

print("------Using the list() constructor to make a List-------")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print("-----list comprehension----")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("-----------You can specify a range of indexes by specifying where to start and where to end the range----------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print("---Check if Item Exists--")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print("-----Change a Range of Item Values----")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print("----------")
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("-----Extend List-----")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("-----Extend List-----")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("----")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("-------")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("---list comprehension -------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
fruits.sort()
print(fruits)
print("---sort in reverse order--")
fruits.sort(reverse = True)
print(fruits)
print("------case-insensitive sort of the list-------")
newlist = fruits.sort(key = str.lower)
print(newlist
print('-------------')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist))
print("-----Customize Sort Function-----")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("------- make a copy of a list by using the : (slice) operator---------")
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Tuples
#A tuple is a collection which is ordered and unchangeable
#Tuples are written with round brackets
#Tuples are used to store multiple items in a single variable
#Tuples can also be created without the parentheses
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#Tuple items can be of any data type and combination of types 
#It is also possible to use the tuple() constructor to make a tuple

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("--- 2nd way to cretae---")
thistuple = "apple", "banana", "cherry"
print(thistuple)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("----- You are allowed to add tuples to tuples----")
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

print("-----packing and unpacking a tuple----")
fruits = ("apple", "banana", "cherry") #packing
(green, yellow, red) = fruits #unpaking
print(green)
print(yellow)
print(red)

print("------")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print("----------")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Sets
#A set is a collection which is unordered, unchangeable*, and unindexed ,and do not allow duplicate values
#Sets are written with curly brackets
#Sets are unordered, so you cannot be sure in which order the items will appear
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#The values True and 1 are considered the same value in sets, and are treated as duplicates
#The values False and 0 are considered the same value in sets, and are treated as duplicates
#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("------------")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print("----------")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("------")
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

print("--------")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
thisset.clear()
print(thisset)

print("-----frozenset-----")
"""
frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""
Method	    Shortcut	    Description
add()	 	                Adds an element to the set
clear()	 	                Removes all the elements from the set
copy()	 	                Returns a copy of the set
difference()	-	        Returns a set containing the difference between two or more sets
difference_update()	-=	    Removes the items in this set that are also included in another, specified set
discard()	 	            Remove the specified item
intersection()	&	        Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	        Returns True if NO items of this set is present in another set
issubset()	    <=	        Returns True if all items of this set is present in another set
 	            <	        Returns True if all items of this set is present in another, larger set
issuperset()	>=	        Returns True if all items of another set is present in this set
 	            >	        Returns True if all items of another, smaller set is present in this set
pop()	 	                Removes an element from the set
remove()	 	            Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	        |	        Return a set containing the union of sets
update()	    |=	        Update the set with the union of this set and others
"""

#Dictionaries
#Dictionaries are used to store data values in key:value pairs
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates
#Dictionaries are written with curly brackets, and have keys and values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print("-----")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.keys()
print(x)

for x, y in thisdict.items():
  print(x, y)

  myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

print("----------")
"""
Method	    Description
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""



