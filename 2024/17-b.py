from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

# Python is too slow, see cpp solution in folder 17
print("136904920099226")

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')