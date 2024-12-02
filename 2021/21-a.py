from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

p1 = int(a[0][-1])
p2 = int(a[1][-1])

p1_score = 0
p2_score = 0
total_rolls = 0
dice = 1
while True:
    p1 += 3 * dice + 1 + 2
    total_rolls += 3
    if p1 > 10:
        p1 = p1 % 10
        if p1 == 0:
            p1 = 10
    p1_score += p1
    if p1_score >= 1000:
        break
    dice += 3

    p2 += 3 * dice + 1 + 2
    total_rolls += 3
    if p2 > 10:
        p2 = p2 % 10
        if p2 == 0:
            p2 = 10
    p2_score += p2
    if p2_score >= 1000:
        break
    dice += 3

print(total_rolls*min(p1_score, p2_score))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')