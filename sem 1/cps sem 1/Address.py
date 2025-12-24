# Name ="Nirlep Boddupally"
# Age_in_years = 18
# height_in_meters = 5.5
# is_student = True
# address =" tngos colony khammam  near bus stand"
# print(f"name:{Name} \nage:Age is:{Age_in_years}\nheidht in meters:{height_in_meters}\nis student:{is_student}\naddress:{address} ")

user=float(input("enter temp:"))
value=input("enter whther c or f or k")
if value=="c":
    new_temp=user*9/5+32
elif value=="f":
    new_temp=user-32*5/9
elif value=="k":
    new_temp=user+275.15
    print(f"the value in c:{new_temp}")    
print(f"the temp {new_temp}")    
    
