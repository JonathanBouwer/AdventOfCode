from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

count = 0

for y in range(len(a)-2):
    for x in range(len(a[0])-2):
        diag = a[y][x] + a[y+1][x+1] + a[y+2][x+2]
        back_diag = a[y+2][x] + a[y+1][x+1] + a[y][x+2]
        if (diag == "MAS" or diag == "SAM") and (back_diag == "MAS" or back_diag == "SAM"):
            count += 1

print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')