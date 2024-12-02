from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

prefix_1, prefix_2, x_range, yrange =  a[0].split(" ")
x_1, x_2 = x_range[2:-1].split("..")
y_1, y_2 = yrange[2:].split("..")
x_min = min(int(x_1), int(x_2))
x_max = max(int(x_1), int(x_2))
y_min = min(int(y_1), int(y_2))
y_max = max(int(y_1), int(y_2))

hit_count = 0

for x in range(1, x_max + 1):
    for y in range(y_min, -y_min):
        pos_x = 0
        pos_y = 0
        x_v = x
        y_v = y
        while True:
            pos_x += x_v
            pos_y += y_v
            if x_v > 0:
                x_v -= 1
            y_v -= 1
            if pos_x >= x_min and pos_x <= x_max and pos_y >= y_min and pos_y <= y_max:
                hit_count += 1
                break
            if pos_x > x_max or pos_y < y_min or (pos_x < x_min and x_v <= 0):
                break

print(hit_count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')