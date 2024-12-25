from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

a = [[int(x) if x != '.' else -9 for x in l] for l in a]

SIZE = len(a)
graph = [[[] for j in range(SIZE)] for i in range(SIZE)]
trail_heads = []

for y in range(SIZE):
    for x in range(SIZE):
        next = a[y][x] + 1
        if next == 1:
            trail_heads.append((x,y))
        if x > 0 and a[y][x-1] == next:
            graph[y][x].append((x-1, y))
        if y > 0 and a[y-1][x] == next:
            graph[y][x].append((x, y-1))
        if x < SIZE - 1 and a[y][x+1] == next:
            graph[y][x].append((x+1, y))
        if y < SIZE - 1 and a[y+1][x] == next:
            graph[y][x].append((x, y+1))

score = 0 
for x,y in trail_heads:
    to_consider = [(x,y)]
    while len(to_consider) > 0:
        x,y = to_consider.pop(0)
        if a[y][x] == 9:
            score += 1
            continue
        to_consider.extend(graph[y][x])

print(score)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')