from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()



print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')