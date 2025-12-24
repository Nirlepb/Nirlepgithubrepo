def distirbute_tasks(server_loads,new_tasks):
    for i in range(new_tasks):
        
        for i in range(len(server_loads)):
                
            if server_loads[i] ==min(server_loads):
                server_loads[i]+=1
                break
            
    return server_loads

server_loads = [10, 5, 2, 8] 
new_tasks = 5 
result=distirbute_tasks(server_loads,new_tasks)     
print(result)
diict = {"name": "Alice", "score": 85}
diict.fromkeys()
