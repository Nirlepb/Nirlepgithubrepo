data=[{"campus_location":"dubai","programs_offered":["engineering","business","arts"],"student_population":4200,"year_established":2015},
      {"campus_location":"Singapore","programs_offered":["computer science","business","media studies"],"student_population":5800,"year_established":2008},
      {"campus_location":"London","programs_offered":["law","history","arts","economics"],"student_population":6100,"year_established":1999},
      {"campus_location":"Sydney","programs_offered":["engineering","business","science"],"student_population":3900,"year_established":2018},
      {"campus_location":"Berlin","programs_offered":["media studies","computer science","arts"],"student_population":5500,"year_established":2012}]

def newest_campus(newcampus):
    max=0
    final=""
    for i in newcampus:
        if i["year_established"]>max:
            max=i["year_established"]
        final=i["campus_location"]    
    return final
def program(all_campus):
    hip=[]
    hip_set=()
    for i in all_campus:
        hip.extend(i["programs_offered"])
        hip_set=set(hip)
    return hip_set
def min_student(student_count):
    campus_name_list=[]
    for i in student_count:
        if i["student_population"]>5000:
            campus_name_list.append(i["campus_location"])
    return campus_name_list
def user_input(campus_list_offered):
    num=0    
    for i in campus_list_offered:
        if user in i["programs_offered"]:
          
            num+=1        
    return num           

    
    
def one_uniqe(uniqe):
    ki=[]
    uni_programs=[]
    for i in uniqe:
        uni_programs.extend(i["programs_offered"])
    for j in uni_programs:
        if uni_programs.count(j)==1:
            ki.append(j)    
    return ki
print(one_uniqe(data))        
print("====================colleage=================")
print("1. Determine the newest campus (the one established most recently.")
print("2.Create a set of all programs offered across all campuses.")
print("3. When a minimum student population number (e.g., 5000) is provided, list the names of all campuses that exceed this population threshold.")
print("4.When a program name (e.g., 'Arts') is given as input, display the number of campuses")
print("5.that offer that programList all the programs that are offered by exactly one of the five campuses (unique programs)")
print("6.exit")
print("===============================================")
while True:
    choice=int(input("ENTER THE CHOICE:"))
    if choice==1:
        print(newest_campus(data))
    if choice==2:
        print(program(data))
    if choice==3:
        print(min_student(data))
    if choice==4:
        user=input("ENTER THE COURCE")
        print(user_input(data))
    if choice==5:
        print(one_uniqe(data)) 
    else:
        break                            
            