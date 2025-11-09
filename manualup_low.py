nip=input("enter a text:")
output=""
for ch in nip:
    if 'A' <= ch <= 'Z':
        output+=chr(ord(ch)+32)
    else:
        continue 
print(output)       