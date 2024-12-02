from utils import load_input
a = load_input(__file__)[0]

from time import perf_counter
t0 = perf_counter()

day_counts = {i: 0 for i in range(9)}
for x in a.split(','):
    day_counts[int(x)] +=1

for n in range(256):
    day_0 = day_counts[0]
    for i in range(8):
        day_counts[i] = day_counts[i+1]
    day_counts[6] += day_0
    day_counts[8] = day_0

print(sum(day_counts.values()))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')