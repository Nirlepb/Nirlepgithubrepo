def  scale_resolutions(resolution,factor):
    factor=0.5
    new_list=[]
   
    for ch in resolution:
        char_res=ch[0]
        char_has=ch[1]
        
        new_res=int(char_res*factor)
        new_has=int(char_has*factor)
        new_tuple=(new_res,new_has)
        new_list.append(new_tuple)
    return new_list   
resolutions = [
    (1920, 1080),
    (1280, 720),
    (2560, 1440)
]
factor = 0.5

# --- Calling the function ---
result = scale_resolutions(resolutions, factor)

# --- Printing the output ---
print(f"Original: {resolutions}")
print(f"Scaled:   {result}") 
        