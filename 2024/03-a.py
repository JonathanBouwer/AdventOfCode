import re

from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

total = 0
for line in a:
    x = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for m in x:
        k = m.split(",")
        l = int(k[0][4:])
        r = int(k[1][:-1])
        total += l * r
    
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')