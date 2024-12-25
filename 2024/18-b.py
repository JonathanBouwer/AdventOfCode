from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

import heapq as hq 

SIZE=71

low = 0
high = len(a)
while high > low + 1:
    walls = set()

    mid = low + (high - low) //  2
    for l in range(mid):
        x,y = a[l].split(",")
        walls.add((int(x),int(y)))

    graph = [[[] for i in range(SIZE)] for j in range(SIZE)]

    for y in range(SIZE):
        for x in range(SIZE):
            if (x,y) in walls:
                continue
            if y > 0 and (x,y-1) not in walls:
                graph[y][x].append((x, y-1))
            if x > 0 and (x-1,y) not in walls:
                graph[y][x].append((x-1, y))
            if y < SIZE-1 and (x,y+1) not in walls:
                graph[y][x].append((x, y+1))
            if x < SIZE-1 and (x+1,y) not in walls:
                graph[y][x].append((x+1, y))

    end_pos = (SIZE-1, SIZE-1)
    base_dist = end_pos[0] + end_pos[1]
    q = [(base_dist, 0, (0,0))]
    hq.heapify(q)
    seen = set()
    while len(q) > 0:
        heuristic, cost, pos = hq.heappop(q)
        if pos in seen:
            continue
        seen.add(pos)

        if pos == end_pos:
            break

        x,y = pos
        h = base_dist - x - y + cost
        for p in graph[y][x]:
            if p in seen:
                continue
            hq.heappush(q, (h, cost+1, p))
    else:
        high = mid
        continue
    low = mid

print(a[low])

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')