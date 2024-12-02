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
paths = set()
twice_node = ''
def bfs(current_node, twice_count, current_path):
    if current_node == 'end':
        paths.add(current_path)
        return

    for child in graph[current_node]:
        was_seen = child in seen
        if child == twice_node:
            if twice_count >= 2:
                continue
            twice_count += 1
        elif was_seen:
            continue

        if child not in upper_keys:
            seen.add(child)

        bfs(child, twice_count, f'{current_path},{child}')

        if child == twice_node:
            twice_count -= 1

        if not was_seen:
            seen.discard(child)

bfs('start', 0, 'start')
for key in graph:
    if key == 'start' or key == 'end' or key in upper_keys:
        continue

    twice_node = key
    bfs('start', 0, 'start')

print(len(paths))
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')