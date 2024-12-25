from utils import load_input
a = load_input(__file__)
a=a[0]

from time import perf_counter
t0 = perf_counter()

files = []
i = 0
id = 0
pos = 0
for i in range(0, len(a)-1, 2):
    l1 = int(a[i])
    files.append((id, pos, l1))
    id += 1
    pos += l1 + int(a[i+1])

files.append((id, pos, int(a[-1])))

compact = []

gaps = []
last_pos = 0

for id, pos, flen in files:
    if pos > last_pos:
        glen =  pos - last_pos
        compact += [0]*glen
        gaps.append((last_pos, glen))
    compact += [id]*flen
    last_pos = pos + flen

for file in reversed(files):
    id, pos, flen = file
    for gid, (gpos, glen) in enumerate(gaps):
        if gpos > pos:
            break

        if glen == 0 or flen > glen:
            continue

        for i in range(flen):
            compact[gpos + i] = id
            compact[pos + i] = 0
        if glen > flen:
            gaps[gid] = (gpos+flen, glen-flen)
        else:
            gaps = gaps[:gid] + gaps[gid+1:]
        break

total = 0
for i, id in enumerate(compact):
    total += id * i
    
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')