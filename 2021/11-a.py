from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

octos = [[int(x) for x in r] for r in a]
HEIGHT = len(octos)
WIDTH = len(octos[0])

def flash(x, y):
    if octos[y][x] > 10:
        return
    for y_1 in range(y-1, y+2):
        if y_1 < 0 or y_1 >= HEIGHT:
            continue
        for x_1 in range(x-1, x+2):
            if x_1 >= 0 and x_1 < WIDTH:
                octos[y_1][x_1] += 1
                if octos[y_1][x_1] == 10:
                    flash(x_1, y_1)

flashes = 0
for step in range(100):
    for y, row in enumerate(octos):
        for x in range(WIDTH):
            row[x] += 1
            if row[x] == 10:
                flash(x, y)

    for row in octos:
        for x in range(WIDTH):
            if row[x] >= 10:
                row[x] = 0
                flashes += 1

print(flashes)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')