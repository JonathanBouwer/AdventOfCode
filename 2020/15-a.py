from time import perf_counter
t0 = perf_counter()

a = [5,1,9,18,13,8,0]

cache = {}

def add_to_cache(k, v):
    if k not in cache:
        cache[k] = [-1, v]
        return
    cache[k][0] = cache[k][1]
    cache[k][1] = v

for i, val in enumerate(a):
    add_to_cache(val, i + 1)

cur = a[-1]
for i in range(len(a), 2020):
    add_to_cache(cur, i)
    prev = cache[cur][0]
    cur = 0 if prev == -1 else i - prev

print(cur)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')
