from operator import mul, sub
def add():
    a = int(input("Enter the number "))
    ask = "yes"
    while (ask == "yes"):
        b = int(input("Enter the number "))
        total = sum([a,b])
        ask = input("Do you want to add another number?:yes/no ")
        print (total)
def subtraction():  
        a = int(input("Enter the number "))
        ask = "yes"
        while (ask == "yes"):
            b = int(input("Enter the number "))
            total =sub([a,b])
            ask = input("Do you want to add another number?:yes/no ")
            print (total) 
def multiplication():
        a = int(input("Enter the number "))
        ask = "yes"
        while (ask == "yes"):
            b = int(input("Enter the number "))
            total=mul(a,b)
            ask = input("Do you want to add another number?:yes/no ")
            print (total) 
def divide():
        a = int(input("Enter the number "))
        ask = "yes"
        while (ask == "yes"):
            b = int(input("Enter the number "))
            total=divmod(a, b)
            ask = input("Do you want to add another number?:yes/no ")
            print (total) 
print("Enter a for addition")
print("Enter s for subtraction")
print("Enter m for multiplication")
print("Enter d for division ")
print("Enter q to quit ")
    
c=input("Enter your choice ")
if c=="a":
    add()
if c=="s":
    subtraction()
if c=="m":
    multiplication()
if c=="d":
    divide()
if c=="q":
    print("quit")
else:
    print("Enter valid option")
    
    
            
