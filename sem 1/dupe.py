def dup(packets):
    dic={}
    for i in packets:
        no=0
        for j in packets:
            if i==j:
                no+=1
                if no>1:
                    dic.update({i:no}) 
    return dic
packets = [1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]        
print(dup( [1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]))

               
            
            