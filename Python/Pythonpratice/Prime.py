num=int(input("Enter the number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num, "Number is not prime")
    else:
            print(num, "Number is prime")

   
    
