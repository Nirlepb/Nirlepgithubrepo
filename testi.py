# n=int(input("enter the number:"))
# x=1

# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print(f"{x} ",end="")
#         x+=1
#     x+=i 
#     print() 
# for i in range(0,n):
#     for j in range(0,n-1-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print(f"{x} ",end="")
#         x+=1
#     print()
#     x+=1    
                  
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
# lis=[9,8,7,6,5,4,3,2,1]
# n=len(lis)

# for i in range(n):
#     current=lis[i]
#     j=i-1
#     while j >= 0 and lis[j] > current:
#         lis[j + 1] = lis[j]
#         j -= 1
        
#     lis[j + 1] = current

# print(lis)
        
    
# n=int(input("enter the number:"))
# x=1

# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print(f"{x} ",end="")
#         x+=1
#     x=i+1 
#     print() 
# for i in range(0,n):
#     for j in range(0,n-1-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print(f"{x} ",end="")
#         x+=1
#     x=i+1   
    # print()
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print("* "*i)
#     print() ;
# def binary_function(n):
#     for i in range(0,n+1):
#         if i%2==0:
#             t_val=1
#         else:
#             t_val=0 
#     row_output = " "        
#     for j in range(0,i+1):
#         current_val = (t_val + j - 1) % 2
#         row_output += str(current_val) + " "
#     print(row_output)
# n_rows = 5
# print(f"The Binary Right Angle Pattern (for n = {n_rows}):")
# binary_function(n_rows)        
# def print_binary_right_angle(n):
    
   
#     for i in range(1, n + 1):
        
#         if i % 2 != 0:
#             start_val = 1
#         else:
#             start_val = 0

        
#         row_output = ""
#         for j in range(1, i + 1):
            
#             current_val = (start_val + j - 1) % 2
#             row_output += str(current_val) + " "

#         print(row_output)


# n_rows = 9
# print(f"The Binary Right Angle Pattern (for n = {n_rows}):")
# print_binary_right_angle(n_rows)  
# C = []
# rows=int(input("enter the number of rows:"))
# cols=int(input("enter the number of cols:"))
# for i in range(rows):
# 	C.append([0]*cols)

# sum=0
# for i in range(5):
#     sum+=i
# print(sum)    '\
# x = 5
# for y in range(1,11):
#     print(x,"* ",y,"= ",x*y)
# for x in range(2,8):
#     for y in range(1,4):
#         print(x*y)   



# li=[[2,3,4],[4,5,6],[8,9,10],[11,12,13]]
# sum=0
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         sum+=li[i][j]
# print(sum)

# li=[[2,3],[4,5]]       
# li1=[[2,9],[5,6]]
# l=[] ## matrix addtion
# for i in range(len(li)):
#     li3=[]
#     for j in range(len(li[i])):
#         n=li[i][j]+li1[i][j]
#         li3.append(n)
#     l.append(li3)       
# print(l)        
# li=[[2,3],[4,5]]       

# l=[] ## matrix addtion
# for i in range(len(li)):
    
#     for j in range(len(li[i])):
#         n=li[i][j]
#         n=li[j][i]    
#         l.append(n)
             
# print(l)       
# def nip(num1,num2):
#     sum=num1+num2
#     return sum
# r=nip(5,6)
# print(r)
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))
# l=[1,5,4]
# len(l)
# l.append(3)
# for i in range(len(l)):
#     if l[i]==5:
#         print(f"the index is") 
            
#         print(i)        
# flowers={'hibiscus':{"unit_price":100,
#                      'colours_available':["red","white","pink","violet","orange","yellow"]},
#          'rose':{'unit_price':200,
#                  'colours_available':['red','white','maroon','yellow']},
#          'marigold':{'unit_price':50,
#                      'colours_available':['orange','yellow']},
#          'dahlia':{'unit_price':150,
#                    'colours_available':['red','white','pink']},
#          'lotus':{'unit_price':300,
#                   'colours_available':['blue','pink','yellow']}
# }
# for flower,detalies in flowers.items():
#     for i in flower:
#     print(i)
# d={'a':1,'b':3,'c':2}
# su=0
# no=len(d)
# for k in d.values():
#     su+=k 
#     avg=su/no
# print(su)
# print(avg)
# l=[15,2,7,25,10]
# max=0
# min=l[0]
# for i in l:
#     if i>max:
#         max=i
#     if i<min:
#         min=i    
# print(max)
# print(min)
# l=[10,10,20,30,40]#find duplicate
# m=[]
# for i in l:
#     if i in m:
#         continue
#     else:
#         m.append(i)
# print(m)     
# l=[10,20,10,20,30,40,50]
# l.sort()

# m=set(l)
# print(m)
# inp=input("======enter the elements in list=========").split(',')
# l=[int(i) for i in inp]
# n=int(input())
# count=0
# for j in l:
#     if j==n:
#         count+=1
# print(f"{l}\n{n}:{count}")                