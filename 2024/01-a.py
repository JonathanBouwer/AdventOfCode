from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

l1 = [int(x.split("   ")[0]) for x in a]
l2 = [int(x.split("   ")[1]) for x in a]

sl1 = sorted(l1)
sl2 = sorted(l2)

diff = 0
for i in range(len(sl1)):
    diff += abs(sl1[i] - sl2[i])

print(diff)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')