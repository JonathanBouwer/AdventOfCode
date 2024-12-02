from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

pairs = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

total = 0
for l in a:
    q = []
    for c in l:
        if c in ['(', '{', '[', '<']:
            q.append(c)
            continue
        match, score = pairs[c]
        if q.pop() != match:
            total += score
            break

print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')