from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

map = []
instructions = []
map_mode = True
pos = (-1, -1)
for y, l in enumerate(a):
    if l == "":
        map_mode = False
        continue

    if map_mode:
        map.append([c for c in l])
        if "@" in l:
            pos = (l.index("@"), y)
    else:
        instructions.extend([c for c in l])
        
def movchr(x, y, dx, dy):
    nx, ny = x+dx, y+dy
    if map[ny][nx] == "#":
        return x, y
    if map[ny][nx] == ".":
        map[ny][nx] = map[y][x]
        map[y][x] = "."
        return nx, ny
    
    # Must be Box
    nnx, nny = movchr(nx, ny, dx, dy)
    if nnx == nx and nny == ny:
        return x, y
    else:
        map[ny][nx] = map[y][x]
        map[y][x] = "."
        return nx, ny
        
for c in instructions:
    dx, dy = 0, 0
    if c == "^":
        dy = -1
    elif c == ">":
        dx = 1
    elif c == "v":
        dy = 1
    elif c == "<":
        dx = -1
    x, y = pos
    pos = movchr(x, y, dx, dy)
    
total = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "O":
            total += 100 * y + x

print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')