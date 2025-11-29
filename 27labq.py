# f=open('27lab.txt','r')
# content=f.read()#makeing it to read 
# l={}#initiating dict
# words=content.split()#split ing the given value


# for i in words:#simple loop
#     if i in l :
#         l[i]+=1
#     else:
#         l[i]=1    
# print(l)       
f=open('27lab.txt','r')
content=f.read()#makeing it to read 
# l={}#initiating dict
# words=content.split()#split ing the given value
line=1
for i in content:#simple loop
    if i=='\n' :
        line+=1
           
print(line)     
