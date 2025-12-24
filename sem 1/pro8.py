nip=[1,3,5,9,20,10]
target=20
for i in range(len(nip)):
    if nip[i]==target:
        print("the target is ",i)
        break
    if i==len(nip)-1:
        print('the target is not found')
    
            