from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

totals = []
for l in a:
    q = []
    for c in l:
        if c in ['(', '{', '[', '<']:
            q.append(c)
            continue
        if q.pop() != pairs[c]:
            break
    else:
        subtotal = 0
        q.reverse()
        for c in q:
            subtotal *= 5
            subtotal += points[c]
        totals.append(subtotal)
        
totals.sort()
print(totals[len(totals) // 2])
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')