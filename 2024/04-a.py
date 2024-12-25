from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

count = 0
HEIGHT = len(a)
WIDTH = len(a[0])

# Horizontal
for y in range(HEIGHT):
    for x in range(WIDTH-3):
        h = a[y][x:x+4]
        if h == "XMAS" or h == "SAMX":
            count += 1

for y in range(HEIGHT-3):
    # Verticals
    for x in range(WIDTH):
        v = a[y][x] + a[y+1][x] + a[y+2][x] + a[y+3][x]
        if v == "XMAS" or v == "SAMX":
            count += 1

    # Diagonals
    for x in range(WIDTH-3): 
        d1 = a[y][x] + a[y+1][x+1] + a[y+2][x+2] + a[y+3][x+3]
        d2 = a[y+3][x] + a[y+2][x+1] + a[y+1][x+2] + a[y][x+3]
        if d1 == "XMAS" or d1 == "SAMX":
            count += 1
        if d2 == "XMAS" or d2 == "SAMX":
            count += 1

print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')