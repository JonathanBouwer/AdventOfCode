from time import perf_counter
t0 = perf_counter()

# All vals are prime
a = [19,1,1,1,1,1,1,1,1,41,1,1,1,1,1,1,1,1,1,523,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,17,13,1,1,1,1,1,1,1,1,1,1,29,1,853,1,1,1,1,1,37,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,23]

M = 1
for val in a:
    M *= val

final_val = 0
for j, val in enumerate(a):
    i = (val - j) % val
    if val == 1:
        continue
    m = (M // val) 
    # TODO: make this fater using extended gcd
    inv = -1
    for n in range(val):
        if (n * m) % val == 1:
            inv = n
            break

    final_val += (i * m * inv) % M

print(final_val % M)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')