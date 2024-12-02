from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

counts = [sum(int(s[i]) for s in a) for i in range(len(a[0]))]    
ga = ''.join('0' if len(a) - c > c else '1' for c in counts)
ep = ''.join('1' if len(a) - c > c else '0' for c in counts)

print(int(ga, 2) * int(ep, 2))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')