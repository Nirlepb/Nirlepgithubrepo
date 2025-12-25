# def fact(n):
    
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n=int(input("enter a number:-"))
# print(fact(n))

# def gcd(a,b):
#     a,b=abs(a),abs(b)
#     if b==0:
#         return a
#     return gcd(b,a%b)
# a=int(input("enter a"))
# b= int (input("enter b"))
# print(gcd(a,b))

# def reverse_string(s):
#     if len(s)==0:
#         return s
#     return reverse_string(s[1:]) +s[0]
# s=input("enter the string")
# print(reverse_string(s))

# def recursive_sum(arr):
#     if not arr:
#         return 0
#     return recursive_sum(arr[1:])+arr[0]
# arr=[]
# j=int(input("enter the number of elements:-"))
# for i in range(j):
#     user=int(input("enter the number:-"))
#     arr.append(user)
# print(recursive_sum(arr))

# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
# n=int(input("enter the number"))
# print(fib(n))

        
    