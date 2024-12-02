from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

grid = [[0 for i in range(1000)] for j in range(1000)]
count = 0

for line in a:
    p1, p2 = line.split(' -> ')
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    if x1 == x2:
        if y2 >= y1:
            start = y1
            end = y2 + 1
        else: 
            start = y2
            end = y1 + 1
        for y in range(start, end):
            grid[y][x1] += 1
            if grid[y][x1] == 2:
                count += 1
        continue
    
    if y1 == y2:
        if x2 >= x1:
            start = x1
            end = x2 + 1
        else: 
            start = x2
            end = x1 + 1
        for x in range(start, end):
            grid[y1][x] += 1
            if grid[y1][x] == 2:
                count += 1
        continue

    if y2 >= y1:
        start = y1
        end = y2 + 1
        x = x1
        if x2 > x1:
            x_inc = 1
        elif x1 > x2: 
            x_inc = -1
    else:
        start = y2
        end = y1 + 1
        x = x2            
        if x2 > x1:
            x_inc = -1
        elif x1 > x2: 
            x_inc = 1
                
    for y in range(start, end):
        grid[y][x] += 1
        if grid[y][x] == 2:
            count += 1
        x += x_inc


print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')