from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

from functools import lru_cache 

@lru_cache(maxsize = 2**16) 
def calc(val, count):
    if count == 0:
        return 1

    if val == 0:
        return calc(1, count - 1)
    elif len(str(val)) % 2 == 0:
        s = str(val)
        mid = len(s)//2
        return calc(int(s[:mid]), count - 1) + calc(int(s[mid:]), count - 1)
    else:
        return calc(val * 2024, count - 1)    

stones = [int(x) for x in a[0].split(" ")]

total = 0
for stone in stones:
    total += calc(stone, 25)
  
print(total)
  
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')