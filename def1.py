def  identify_intruders(attempts,authorized):
    intruders={"."}
    for i in attempts:
        if i not in authorized:
            intruders.add(i)
    return intruders        
attempts = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
authorized = {"alice", "bob", "frank", "grace"}
print(identify_intruders(attempts,authorized))
