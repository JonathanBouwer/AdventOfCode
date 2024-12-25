from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def gen(x):
    x = ((x<<6) ^ x) % 16777216
    x = ((x>>5) ^ x) % 16777216
    return ((x<<11) ^ x) % 16777216

sequences = {}
for n, v in enumerate(a):
    s = int(v)
    key = ()
    for i in range(4):
        prev = s%10
        s = gen(s)
        key += (s%10 - prev,)
    # Unrolling loop for performance
    for i in range(998):
        prev = s%10
        s = gen(s)
        cur = s%10
        # might be a bug here if best option is i=4 (i.e. we ignore the first sequence)
        key = key[1:] + (cur - prev,)
        if key not in sequences:
            sequences[key] = {}
        if n not in sequences[key]:
            sequences[key][n] = cur

        s = gen(s)
        cur2 = s%10
        key = key[1:] + (cur2 - cur,)
        if key not in sequences:
            sequences[key] = {}
        if n not in sequences[key]:
            sequences[key][n] = cur2

best_key = 0
best = 0
for k,v in sequences.items():
    t = sum(v.values())
    if t > best:
        best_key = k
        best = t

# print(best_key)
print(best)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')