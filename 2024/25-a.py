from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

locks = []
keys = []

a.append("")

cur_lines = []
for l in a:
    if l != "":
        cur_lines.append(l)
        continue
    s = [0 for i in range(5)]
    for cl in cur_lines[1:-1]:
        for i in range(5):
            if cl[i] == "#":
                s[i] += 1
    if cur_lines[0] == "#####":
        locks.append(s)
    else:
        keys.append(s)
    cur_lines = []

count = 0
for k in keys:
    for l in locks:
        for i in range(5):
            if k[i] + l[i] > 5:
                break
        else:
            count += 1

print(count)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')