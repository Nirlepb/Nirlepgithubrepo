def find_first(log_data):
    
    for tu in log_data:
        if tu[1]=="ERROR":
            print(tu[0])
            break 
    return find_first 
log_data = [('08:30:01', 'INFO', 'Server started'),
 ('08:30:05', 'WARN', 'Low disk space'),
 ('08:31:10', 'INFO','User login'),
 ('08:32:00', 'ERROR','data base connection failed' ),
 ('08:32:01', 'INFO', 'Retrying connection...'),
 ('08:33:00', 'ERROR', 'Authentication service timeout')
 ]      
result=find_first(log_data)
print(f"the ans is {result}")