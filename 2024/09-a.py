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

last_pos = 0
end_file = len(files) - 1
for i in range(len(files)):
    id, pos, len1 = files[i]
    if len1 == 0:
        break

    for j in range(last_pos, pos):
        id2, pos2, len2 = files[end_file]
        compact.append(id2)
        files[end_file] = (id2, pos2, len2-1)
        if len2 == 1:
            end_file -= 1

    id, pos, len1 = files[i]
    compact += [id] * len1
    last_pos = pos + len1

total = 0
for i, id in enumerate(compact):
    total += id * i
    
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')