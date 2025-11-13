def nir(a):#i am difing function
    ni={}# an emty dic
    for i in a:#for i in some value of a 
        if i in ni:# and if i also in dictonary
            ni[i]+=1#then add the number
        else:
            ni[i]=1#else giving number
    print(ni)         
n=[1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]
nir(n)
            
    
                