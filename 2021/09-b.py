from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

heights = [[int(c) for c in x] for x in a]
in_basin = [[c == '9' for c in x] for x in a]

ROWS = len(heights)
COLS = len(heights[0])

def flood_fill(x, y):
    if y < 0 or x < 0 or x >= COLS or y >= ROWS or in_basin[y][x]:
        return 0

    val = heights[y][x]
    in_basin[y][x] = True
    return 1 + flood_fill(x+1,y) + flood_fill(x-1,y) + flood_fill(x,y+1) + flood_fill(x,y-1)

basin_sizes = []
for y in range(ROWS):
    for x in range(COLS):
        if in_basin[y][x]:
            continue

        basin_size = flood_fill(x,y)
        if basin_size > 0:
            basin_sizes.append(basin_size)
        
basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')