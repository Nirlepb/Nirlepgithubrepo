def file_write():
   f = open("ni.txt","w")
   user=input("enter the text you whant to enter:-")
   f.write(user)
   print("file sucessfully updated👍")
   
def file_read():
    f =open("ni.txt",'r')
    result=f.readline()
    print(result)
    print("file read✌️")  
def file_append():
    f=open("ni.txt","a")
    user=input("enter the text to append:-")
    f.write(user + "\n")

    print("appended ")
def search():
    word=input("enter the target word:_")
    count=0
    f=open("ni.txt","r")
    for line in f:
        count+= line.lower().count(word.lower())
    print(f"'{word}' found {count} times.")    
            
print("""
       1. Write data to file

       2. Read data from file

       3. Append data to file

       4. Search a word in file

        5.Exit
      
      
      
      
      """)            
while True:
    choice=int(input("----------enter the choice------------"))
    if choice==1:
        file_write()
    elif choice==2:
        file_read()
    elif choice==3:
        file_append()
    elif choice==4:
        search()
    elif choice==5:
        break
    else:
        print("enter a corect choice😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️")            