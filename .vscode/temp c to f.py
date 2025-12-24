temp=float(input("enter the temperature "))
unit=input("c or f:")
if unit=="c":
    temp=(temp*9/5)+32
    unit="f"
elif unit=="f":
    temp=(temp-32)*5/9
    unit="c"
print(f"temperature:{temp}{unit}")    