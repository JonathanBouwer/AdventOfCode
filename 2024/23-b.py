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

best_party = []
nodes = [x for x in graph.keys()]
for i in range(len(nodes)):
    for j in range(i, len(nodes)):
        lan_party = (graph[nodes[i]] & graph[nodes[j]])
        lan_party.add(nodes[i])
        lan_party.add(nodes[j])
        if len(lan_party) <= len(best_party):
            continue
        disconnected = False
        for k in lan_party:
            for kk in lan_party:
                if k == kk:
                    continue
                if kk not in graph[k]:
                    disconnected = True
                    break
            if disconnected:
                break

        if not disconnected:
            best_party = lan_party

print(",".join(sorted(best_party)))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')