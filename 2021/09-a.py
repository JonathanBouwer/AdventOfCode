from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

heights = [[int(c) for c in x] for x in a]

ROWS = len(heights)
COLS = len(heights[0])


def is_low_point(x, y):
    val = heights[y][x]
    
    if y > 0 and val >= heights[y-1][x]:
        return False
    if y < ROWS - 1 and val >= heights[y+1][x]:
        return False
    if x > 0 and val >= heights[y][x-1]:
        return False
    if x < COLS - 1 and val >= heights[y][x+1]:
        return False
    
    return True

total = 0
for y in range(ROWS):
    for x in range(COLS):
        if is_low_point(x, y):
            total += heights[y][x] + 1
            
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')