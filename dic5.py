def nip(a,b):
    fake=set()
    for i in a:
        if i not in b:
            fake.add(i)
    return fake
ad = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
bc = {"alice", "bob", "frank", "grace"}
result=nip(ad,bc)
print(result)
