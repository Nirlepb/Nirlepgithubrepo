
def fact(n):#first we defined function
   
    if n==0:#if n==0 it should end and print 1
        print(f"returned the value 1")
        return 1 #base
    else:
        print(f"retuned {n-1}")
        return n*fact(n-1)#recurive#if it is not zero then factorial n*fact(n-1)
n=int(input("enter the number:"))    #user should give input
print(f"the factoral of numbers:{fact(n)}")#printing the output
