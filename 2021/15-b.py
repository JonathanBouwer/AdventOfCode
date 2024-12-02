from utils import load_input
a = load_input(__file__)

from heapq import heappush, heappop
from time import perf_counter
t0 = perf_counter()

c = [[int(x) for x in r] for r in a]

cave = []
for y_1 in range(5):
    for y in range(len(c)):
        new_row = []
        for x_1 in range(5):
            for x in range(len(c[0])):
                new_val = c[y][x] + y_1 + x_1
                if new_val > 9:
                    new_val %= 9
                new_row.append(new_val)
        cave.append(new_row)

HEIGHT = len(cave) - 1
WIDTH = len(cave[0]) - 1

queue = []
heappush(queue, (0,0,0))

seen = [[False for d in c] for c in cave]

while True:
    val,x,y = heappop(queue)
    if y == HEIGHT and x == WIDTH:
        print(val)
        break
    if x < WIDTH and not seen[y][x+1]:
        seen[y][x+1] = True
        heappush(queue, (val+cave[y][x+1],x+1,y))
    if x > 0 and not seen[y][x-1]:
        seen[y][x-1] = True
        heappush(queue, (val+cave[y][x-1],x-1,y))
    if y < HEIGHT and not seen[y+1][x]:
        seen[y+1][x] = True
        heappush(queue, (val+cave[y+1][x],x,y+1))
    if y > 0 and not seen[y-1][x]:
        seen[y-1][x] = True
        heappush(queue, (val+cave[y-1][x],x,y-1))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')