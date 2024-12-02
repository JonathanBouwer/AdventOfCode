from utils import load_input, parse_int
a = load_input(__file__, parse_int)

from time import perf_counter
t0 = perf_counter()

print(len([1 for i in range(1, len(a)) if a[i] > a[i - 1]]))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')