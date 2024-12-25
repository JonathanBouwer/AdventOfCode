from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

graph = {}

for l in a:
    c1,c2 = l.split("-")
    if c1 not in graph:
        graph[c1] = set()
    graph[c1].add(c2)
    if c2 not in graph:
        graph[c2] = set()
    graph[c2].add(c1)

tree_cons = set()
for k, v in graph.items():
    if k[0] != 't':
        continue
    for con in v:
        for con2 in graph[con]:
            if con2 == k or con2 not in v:
                continue
            tree_cons.add(",".join(sorted([k, con, con2])))

print(len(tree_cons))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')