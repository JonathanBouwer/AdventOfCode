from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

graph = {}
upper_keys = set()
for l in a:
    start, end = l.split('-')
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(end)
    graph[end].append(start)
    upper_keys.add(start.upper())
    upper_keys.add(end.upper())
    
seen = set(['start'])
def bfs(current_node='start'):
    if current_node == 'end':
        return 1
        
    total = 0
    for child in graph[current_node]:
        was_seen = child in seen
        if was_seen and not child in upper_keys:
            continue
        seen.add(child)
        total += bfs(child)
        if not was_seen:
            seen.remove(child)
    return total

print(bfs())

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')