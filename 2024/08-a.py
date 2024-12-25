from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

nodes = {}
for y in range(len(a)):
    for x in range(len(a[0])):
        freq = a[y][x]
        if freq != '.':
            if freq not in nodes:
                nodes[freq] = []
            nodes[freq].append((x,y))

antis = set()

for freq in nodes:
    fnodes = nodes[freq]
    for i in range(len(fnodes)):
        for j in range(i+1, len(fnodes)):
            n1 = fnodes[i]
            n2 = fnodes[j]

            dx = n1[0] - n2[0]
            dy = n1[1] - n2[1]

            a1x = n1[0]+dx
            a1y = n1[1]+dy
            if a1x >= 0 and a1x < len(a[0]) and a1y >= 0 and a1y < len(a):
                antis.add((a1x, a1y))

            a2x = n2[0]-dx
            a2y = n2[1]-dy
            if a2x >= 0 and a2x < len(a[0]) and a2y >= 0 and a2y < len(a):
                antis.add((a2x, a2y))

print(len(antis))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')