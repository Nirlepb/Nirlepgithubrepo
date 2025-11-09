text=input("enter the text:")
count=0
count1=0
total=0
for t in text:
    ascii_values=ord(t)
    if ascii_values in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
        count+=1
    else:
        count1+=1   
total=count+count1 
avg=count/total        
print("Number of vowels:", count)  
print("the avg: " ,avg)         