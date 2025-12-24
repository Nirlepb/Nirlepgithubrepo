i=int(input("enter the first number:"))
print("1.square\n 2.squre root\n 3.cube")
opp=int(input("enter the operation you want to perform:"))
if opp==1:
    print(i**2)
elif opp==2:
    print(i**0.5)
elif opp==3:
    print(i**3)        
else:
    print("invalid operation")    