n=int(input("enter the number:"))
x=1

for i in range(0,n):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range(0,n-i):
        print(f"{x} ",end="")
        x+=1
    x=i 
    print() 
for i in range(0,n):
    for j in range(0,n-1-i):
        print(" ",end="")
    for k in range(0,i+1):
        print(f"{x} ",end="")
        x+=1
    print()
    x=1   