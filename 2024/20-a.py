from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

graph = [[-1 for i in range(len(a[0]))] for j in range(len(a))]

start_pos = (-1, -1)
end_pos = (-1,-1)

HEIGHT = len(a)
WIDTH = len(a[0])

for y in range(HEIGHT):
    for x in range(WIDTH):
        if a[y][x] == "#":
            continue
        elif a[y][x] == "S":
            start_pos = (x,y)
        elif a[y][x] == "E":
            end_pos = (x,y)

true_dist = 0
seen = set()
while start_pos != end_pos:
    x,y = start_pos
    graph[y][x] = true_dist
    true_dist += 1
    seen.add((x,y))
    if a[y][x+1] != "#" and (x+1,y) not in seen:
        start_pos = (x+1,y)
    elif a[y-1][x] != "#" and (x,y-1) not in seen:
        start_pos = (x,y-1)
    elif a[y][x-1] != "#" and (x-1,y) not in seen:
        start_pos = (x-1,y)
    elif a[y+1][x] != "#" and (x,y+1) not in seen:
        start_pos = (x,y+1)

graph[end_pos[1]][end_pos[0]] = true_dist

RANGE = 2
new_costs = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        dist = graph[y][x]
        if dist < 0:
            continue
        for dy in range(-RANGE, RANGE+1):
            ny = y+dy
            if ny < 0 or ny > HEIGHT-1:
                continue
            ady = abs(dy)
            for dx in range(-RANGE+ady, RANGE+1-ady):
                nx = x+dx
                if nx < 0 or nx > WIDTH-1:
                    continue

                ddist = graph[ny][nx]
                if ddist < dist:
                    continue

                # Saving may be negative but we ignore it later so it's fine
                saving = ddist - dist - ady - abs(dx)
                if saving not in new_costs:
                    new_costs[saving] = 0
                new_costs[saving] += 1
                    
count = 0
for k, v in new_costs.items():
    if k >= 100:
        count += v
print(count)
                
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')