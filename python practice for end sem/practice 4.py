data = {
        "B201": {"Route": "Route A", "Trips": 42, "Delay": 3, "Depot": "Central"},
        "B202": {"Route": "Route B", "Trips": 35, "Delay": 6, "Depot": "North"},
        "B203": {"Route": "Route C", "Trips": 50, "Delay": 2, "Depot": "Central"},
        "B204": {"Route": "Route A", "Trips": 28, "Delay": 8, "Depot": "South"},
        "B205": {"Route": "Route D", "Trips": 45, "Delay": 4, "Depot": "East"}
    }
def find_all_data(bus):
    bus_id=(input("enter the bus id_--_"))
    for id,detalies in bus.items():
        if bus_id in bus:
            print(bus[bus_id])
        else:
            print("ID not found!")
    return  bus
print(find_all_data(data))       