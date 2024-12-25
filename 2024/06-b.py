from utils import load_input
a = load_input(__file__)

from time import perf_counter, sleep
t0 = perf_counter()

a = [[c for c in l] for l in a]

SIZE = len(a)

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

g = guard_pos
d = dir
path = set()
while True:
    x,y = g
    path.add((x,y))
    if d == 0:
        if y == 0:
            break
        x_n,y_n = x,y-1
    elif d == 1:
        if x == SIZE-1:
            break
        x_n,y_n = x+1,y
    elif d == 2:
        if y == SIZE-1:
            break
        x_n,y_n = x,y+1
    elif d == 3:
        if x == 0:
            break
        x_n,y_n = x-1,y
    
    if a[y_n][x_n] == "#":
        d = (d + 1)%4
        continue
    g = x_n,y_n

loops = 0
for ly in range(SIZE):
    for lx in range(SIZE):
        print("\r", round(100*(ly*SIZE+lx)/(SIZE**2),2), "%", end="")
        if a[ly][lx] != ".":
            continue
        elif (lx,ly) not in path:
            continue

        a[ly][lx] = "#"
        x,y = guard_pos
        d = dir
        seen = set() 

        while True:
            if (x,y,d) in seen:
                loops += 1
                break

            if d == 0:
                if y == 0:
                    break
                x_n,y_n = x,y-1
            elif d == 1:
                if x == SIZE-1:
                    break
                x_n,y_n = x+1,y
            elif d == 2:
                if y == SIZE-1:
                    break
                x_n,y_n = x,y+1
            elif d == 3:
                if x == 0:
                    break
                x_n,y_n = x-1,y
            
            if a[y_n][x_n] == "#":
                d = 0 if d == 3 else (d + 1)
                continue
            seen.add((x,y,d))
            x,y = x_n,y_n

        a[ly][lx] = "."

print("\r100%             ")
print(loops)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')