pie=int(input("Enter the no of slice"))
people=int(input("Enter the no of people"))
perhead=int(pie/people)
print("No of slice per head is :",perhead)
total=int(people*perhead)
if pie>total:
    print("Sufficient slice")
else:
    print("Insufficient slice")
