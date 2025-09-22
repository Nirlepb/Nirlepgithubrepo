distance=float(input("enter the number:"))
unit=input("km or m:")

if unit=="km":
    distance=distance*0.6213
    unit="m"
elif unit=="m":
    distance=distance*1.609
    unit="km"
print(f"distance:{distance}{unit}")    
