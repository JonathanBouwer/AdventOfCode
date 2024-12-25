from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

a = [[c for c in l] for l in a]

guard_pos = -1,-1

for y in range(len(a)):
    for x in range(len(a[0])):
        if a[y][x] == "^":
            guard_pos = x,y
            break
    else:
        continue
    break

dir = 0 # 0 Up, 1 Right, 2 Down, 3 Left

seen = set()
while True:
    x,y = guard_pos
    seen.add((x,y))
    if dir == 0:
        if y == 0:
            break
        x_n,y_n = x,y-1
    if dir == 1:
        if x == len(a)-1:
            break
        x_n,y_n = x+1,y
    if dir == 2:
        if y == len(a)-1:
            break
        x_n,y_n = x,y+1
    if dir == 3:
        if x == 0:
            break
        x_n,y_n = x-1,y
    
    if a[y_n][x_n] == "#":
        dir = (dir + 1)%4
        continue
    guard_pos = x_n,y_n
        
print(len(seen))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')