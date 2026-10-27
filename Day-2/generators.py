#Generators are functions that can pause and resume their execution.
#When a generator function is called, it returns a generator object, which is an iterator
#Generators allow you to iterate over data without storing the entire dataset in memory
#Instead of using return, generators use the yield keyword

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

print("--------------")
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen)) #You can manually iterate through a generator using the next() function
print(next(gen))
print(next(gen))

print("------------")
total = sum(x * x for x in range(10)) #generator expression
print(total)

#The send() method allows you to send a value to the generator
print("------------")
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#The close() method stops the generator
print("------------")
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

