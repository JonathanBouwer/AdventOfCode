from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def filter_vals(is_lcb):
    vals = [s for s in a]
    i = 0
    while len(vals) > 1:
        bit_sum = sum(int(v[i]) for v in vals)
        exp = 0 if len(vals) - bit_sum > bit_sum else 1
        exp =  1 - exp if is_lcb else exp
        vals = [val for val in vals if val[i] == str(exp)]
        i += 1
    return vals[0]
        
print(int(filter_vals(True), 2) * int(filter_vals(False), 2))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')