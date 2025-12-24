a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))
c = int(input("enter the value of c :"))
#d is "descriminant"
d = (b**2-4*a*c)
#there are 2 roots so name them root1,root2
root1 = (-b+d**(0.5))/(2*a)
root2 = (-b-d**(0.5))/(2*a)
print(f"the roots are {root1} ,{root2}")