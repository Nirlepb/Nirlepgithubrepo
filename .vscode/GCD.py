def gcd_f(a,b):
    a,b=abs(a),abs(b)
    if b==0:
        return a
    else:
      return  gcd_f(b,a%b)
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))  
ans=gcd_f(a,b)
print(f"the gcd:{ans}")        
