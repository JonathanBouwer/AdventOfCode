from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

from functools import lru_cache 

designs = set(a[0].split(", "))

@lru_cache
def count_possible(d):
    if len(d) == 0:
        return 0

    total = 0
    if d in designs:
        total += 1

    for i in range(1, len(d)):
        if d[:i] in designs:
            total += count_possible(d[i:])
            
    return total

count = 0
for d in a[2:]:
    count += count_possible(d)
        
print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')