v1=int(input("Enter a Number"))
v2=int(input("Enter a Number"))
v3=int(input("Enter a Number"))

if v1 > v2 and v1 > v3:
    print(f"{v1} is bigger than {v2} and {v3}")
elif v2 > v3:
    print(f"{v2} is bigger than {v1} and {v3}")
else: 
    print(f"{v3} is bigger than {v1} and {v2}")
