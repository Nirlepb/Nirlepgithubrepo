data={
    "B201":["RouteA",42,3,"central"],
    "B202":["RouteB",35,6,"North"],
    "B203":["RouteC",50,2,"Central"],
    "B204":["RouteA",28,8,"South"],
    "B205":["RouteD",45,4,"East"],
}
ID=[]
for i in data.keys():
    ID.append(i)
def qu2(bus_id):
    trips_complted=[]
    for i in data.values():
        trips_complted.append(i[0])
    n=len(trips_complted)
    for i in range(n):
         for j in range(0,n-i-1):
            if trips_complted[j]<=trips_complted[j+1]:
                continue
            else:
                trips_complted[j],trips_complted[j+1]=trips_complted[j+1],trips_complted[j]
                bus_id[j],bus_id[j+1]=bus_id[j+1],bus_id[j]
    return bus_id
def question3(list_routes):
    route_name = input("Enter the name of the route: ")
    for bus_id in data:
        if data[bus_id][0] == route_name:
            list_routes.append(bus_id)
    return list_routes
print(question3([]))
             
                
        
    