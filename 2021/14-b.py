from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

rules = {}
pair_counts = {}
for l in a[2:]:
    key, val = l.split(' -> ')
    rules[key] = val 
    pair_counts[key] = 0

for j in range(len(a[0]) - 1):
    key = a[0][j] + a[0][j + 1]
    pair_counts[key] += 1

for i in range(40):
    new_pair_counts = {k: 0 for k in pair_counts.keys()}
    for k, v in pair_counts.items():
        key_1 = k[0] + rules[k]
        key_2 = rules[k] + k[1]
        new_pair_counts[key_1] += pair_counts[k]
        new_pair_counts[key_2] += pair_counts[k]
    pair_counts = new_pair_counts

counts = {c[1]: 0 for c in pair_counts.keys()}
counts[a[0][0]] = 1
for c, val in pair_counts.items():
    counts[c[1]] += val

low = min(counts.values())
high = max(counts.values())
print(high - low)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')