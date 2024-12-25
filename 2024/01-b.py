from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

l1 = [int(x.split("   ")[0]) for x in a]
l2 = [int(x.split("   ")[1]) for x in a]

d2 = {}

for x in l2:
    if x not in d2:
        d2[x] = 0
    d2[x] += 1

diff = 0
for x in l1:
    if x not in d2:
        continue
    diff += x * d2[x]

print(diff)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')