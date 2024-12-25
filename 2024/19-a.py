from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

from functools import lru_cache 

designs = set(a[0].split(", "))

@lru_cache
def is_possible(d):
    if len(d) == 0:
        return False

    if d in designs:
        return True
    
    for i in range(len(d)):
        if d[:i] in designs and is_possible(d[i:]):
            return True
            
    return False

count = 0
for d in a[2:]:
    if is_possible(d):
        count += 1
        
print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')