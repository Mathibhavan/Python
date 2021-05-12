from _ast import If

num1=input("Enter the num1")
num2=input("Enter the num2")
num3=input("Enter the num3")
if num1>num2 and num1>num3:
    print(num1)
if num2>num1 and num2>num3:
    print(num2)
if num3>num1 and num3>num1:
    print(num3)