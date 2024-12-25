from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def gen(x):
    x = ((x<<6) ^ x) % 16777216
    x = ((x>>5) ^ x) % 16777216
    return ((x<<11) ^ x) % 16777216

total = 0
for v in a:
    s = int(v)
    # Unrolling loop improves performance
    for i in range(500):
        s = gen(s)
        s = gen(s)
        s = gen(s)
        s = gen(s)
    total += s
    
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')