def find_freeplace(car: list, car_cells: list, bus_cells: list):
    if car[2] == 'A':
        for cell in range(len(car_cells)):
            if car_cells[cell] <= car[0]: return 'A', cell
    for cell in range(len(bus_cells)):
        if bus_cells[cell] <= car[0]: return 'B', cell
    return -1


with open('26.txt', 'r') as FILE:
    N, L, M = [int(i) for i in FILE.readline().split(' ')]
    clients = [i.split(' ') for i in FILE.readlines()]
    for c in range(len(clients)):
        clients[c][0] = int(clients[c][0])
        clients[c][1] = int(clients[c][1])
        clients[c][2] = clients[c][2].replace('\n', '')
clients.sort(key= lambda x: x[0])
print(clients)
clients.sort()
print(clients)
car_cells = [0] * L
bus_cells = [0] * M
failed = 0
parked_buses = 0

for i in range(1441):
    while clients and clients[0][0] == i:
        client = clients.pop(0)
        place = find_freeplace(client, car_cells, bus_cells)
        if place == -1: failed += 1
        else:
            if client[2] == 'B': parked_buses += 1

            if place[0] == 'A': car_cells[place[1]] = i + client[1]
            else: bus_cells[place[1]] = i + client[1]
print(parked_buses, failed)