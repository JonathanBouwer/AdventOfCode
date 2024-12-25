from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

import heapq as hq 

# E = 0, S = 1, W = 2, N = 3
start_pos = (-1, -1, -1)
end_pos = (-1,-1)

# Elements: (x, y, dir, cost)
graph = [[[[] for k in range(4)] for i in range(len(a[0]))] for j in range(len(a))]

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == "#":
            continue
        elif a[y][x] == "S":
            start_pos = (x,y,0)
        elif a[y][x] == "E":
            end_pos = (x,y)
        
        graph[y][x][0].append(((x,y,1),1000))
        graph[y][x][0].append(((x,y,3),1000))
        graph[y][x][1].append(((x,y,0),1000))
        graph[y][x][1].append(((x,y,2),1000))
        graph[y][x][2].append(((x,y,1),1000))
        graph[y][x][2].append(((x,y,3),1000))
        graph[y][x][3].append(((x,y,0),1000))
        graph[y][x][3].append(((x,y,2),1000))
        
        if a[y][x+1] != "#": # East
            graph[y][x][0].append(((x+1,y,0),1))
        if a[y-1][x] != "#": # South
            graph[y][x][1].append(((x,y-1,1),1))
        if a[y][x-1] != "#": # West
            graph[y][x][2].append(((x-1,y,2),1))
        if a[y+1][x] != "#": # North
            graph[y][x][3].append(((x,y+1,3),1))

queue = [(0, start_pos)]
hq.heapify(queue) 
seen = set()
seen.add(start_pos)
while True:
    cost, pos = hq.heappop(queue) 
    seen.add(pos)
    x, y, dir = pos
    if (x,y) == end_pos:
        print(cost)
        break

    for connection in graph[y][x][dir]:
        p, ccost = connection
        if p in seen:
            continue
        hq.heappush(queue, (cost+ccost, p)) 

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')