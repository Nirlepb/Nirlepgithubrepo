# n=int(input("enter the number:"))
# x=1
# for i in range(0,n):
#     for j in range(0,n-1-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print(f"{x} ",end="")
#         x+=1
#     print()
#     x=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i-1):
#         print(f"{x} ",end="")
#         x+=1
#     x=1 
#     print()               
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print("* "*i)
#     print()
#bubble sort
# list1=[3,2,1]
# n=len(list1)

# for i in range(n):
#     for j in range(n-1):
        
#         if list1[j]<list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
        
# print(list1)
# by using built
# list1=[3,2,1]
# list1.sort()
# print(list1) 
lis=[9,8,7,6,5,4,3,2,1]
n=len(lis)

for i in range(n):
    current=lis[i]
    j=i-1
    while j >= 0 and lis[j] > current:
        lis[j + 1] = lis[j]
        j -= 1
        
    lis[j + 1] = current

print(lis)
        
    
