data ={
        "B201": ["RouteA",42,3,"Central"],
        "B202": ["RouteB",35,6,"North"],
        "B203": ["RouteC",50,2,"Central"],
        "B204": ["RouteA",28,8,"South"],
        "B205": ["RouteD",45,4,"East"],}
IDS=[]
for i in data.keys():
        IDS.append(i)
def question2(bus_ids):
    trips_completed=[]
    for i in data.keys():
        bus_ids.append(i)
    for i in data.values():
        trips_completed.append(i[1])
    for i in range(0,len(trips_completed)):
        for j in range(0,len(trips_completed)-1-i):
            if trips_completed[j]<=trips_completed[j+1]:
                continue
            else:
                trips_completed[j],trips_completed[j+1]=trips_completed[j+1],trips_completed[j]
                bus_ids[j],bus_ids[j+1]=bus_ids[j+1],bus_ids[j]
    return bus_ids

def question3(list_routes):
    route_name=input("Enter the name of the route:")
    n=0
    for i in data.values():
        if i[0]==route_name:
            list_routes.append(IDS[n])
        n+=1
    return list_routes

def question4(dicct):
    depots={}
    total_trips={}
    for i in data.values():
        if i[2]<5:
            if i[3] in depots:
                depots[i[3]]+=1
            else:
                depots[i[3]]=1
    for i in data.values():
        if i[2]<5:
            if i[3] in total_trips:
                total_trips[i[3]]+=i[1]
            else:
                total_trips[i[3]]=i[1]
    for i in data.values():
        if i[3] in depots:
            dicct[i[3]]=total_trips[i[3]]/depots[i[3]]
    return dicct

def question5(high_reliability):
    n=0
    for i in data.values():
        if i[1]>=40 and i[2]<4:
            high_reliability.append(IDS[n])
        n+=1
    return high_reliability

print("--------------question2----------------")
print(question2([]))
print("--------------question3----------------")
print(question3([]))
print("--------------question4----------------")
print(question4({}))
print("--------------question5----------------")
print(question5([]))
print("---------------------------------------")