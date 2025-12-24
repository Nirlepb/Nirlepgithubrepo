marks_list=[]
def add_marks(marks_list):
    hi=int(input("enter number of marks you need to enter:"))
    for i in range(hi):
        user=int(input("enter the marks(0-100):-"))
        marks_list.append(user)
    return marks_list
# add_marks(marks_list)
def display(marks_list):
    if not marks_list:
        print("no marks entered")
    else:
        print("marks",marks_list)    
    return marks_list
# display(marks_list)
# print(display(marks_list))    
def find_max(marks_list):
    max1=0
    for mark in marks_list:
        if mark>max1:
            max1=mark
    return max1
# print(find_max(marks_list))    
def lower_min(marks_list):
    min=1000
    for marks in  marks_list:
        if marks<min:
            min=marks
    return min
def seraching(marks_list):
    value=int(input("enter the target value:"))
    
    for mark in range(len(marks_list)):
        if mark==value:
            print("it is there",marks_list[mark])
        else :
            print("not found")
    return mark

# print(seraching(marks_list,value))           
def sort_marks(marks_list):
    n=len(marks_list)
    for i in range(n):
        for j in range(0,n-i-1):
            #
            if marks_list[j]>marks_list[j+1]:
                marks_list[j],marks_list[j+1]=marks_list[j+1],marks_list[j]
    return marks_list            

while True:
    print("""
            1. Add Student Mark
            2. Display All Marks
            3. Find Highest Mark
            4. Find Lowest Mark
            5 Search for a Mark
            6. Sort Marks
            7. Exit""")
    user1=int(input("enter the operation needed for this"))
    if user1==1:
        add_marks(marks_list)
    if user1==2:
        print(display(marks_list))
    if user1==3:
        print(find_max(marks_list))
    if user1==4:
        print(lower_min(marks_list))
    if user1==5:
        print(seraching(marks_list))
    if user1==6:
        print(sort_marks(marks_list))
    if user1==7:
        break        
                
            
            
        
        
    


    