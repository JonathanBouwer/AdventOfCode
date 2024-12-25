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
        row = []
        for c in l:
            if c == "@":
                row.extend(["@", "."])
            elif c == "O":
                row.extend(["[", "]"])
            else:
                row.extend([c, c])
        map.append(row)
        if "@" in row:
            pos = (row.index("@"), y)
    else:
        instructions.extend([c for c in l])

def can_mov(x, y, dx, dy):
    nx, ny = x+dx, y+dy
    v = map[ny][nx]
    if v == "#":
        return False
    if v == ".":
        return True

    # Must be box
    if dy == 0:
        return can_mov(nx, ny, dx, dy)
    if v == "[":
        return can_mov(nx, ny, dx, dy) and can_mov(nx+1, ny, dx, dy) 
    else:
        return can_mov(nx-1, ny, dx, dy) and can_mov(nx, ny, dx, dy)
   
def movchr(x, y, dx, dy, skip):
    nx, ny = x+dx, y+dy
    v = map[ny][nx]
    if v == "#":
        return x, y
    if v == ".":
        map[ny][nx] = map[y][x]
        map[y][x] = "."
        return nx, ny

    # Must be box, skip implies already checked can_mov
    if not skip and not can_mov(x, y, dx, dy):
        return x, y

    if dy != 0:
        if map[ny][nx] == "[":
            movchr(nx+1, ny, dx, dy, True)
        else:
            movchr(nx-1, ny, dx, dy, True)
    
    movchr(nx, ny, dx, dy, True)
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
    pos = movchr(x, y, dx, dy, False)
    
total = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "[":
            total += 100 * y + x

print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')