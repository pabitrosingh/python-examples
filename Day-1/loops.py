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