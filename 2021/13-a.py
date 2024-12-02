from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

points = set()
instructions = []
is_instructions = False
for l in a:
    if l == '':
        is_instructions = True
        continue
    if is_instructions:
        inst,val = l.split('=')
        direction = inst.split(' ')[-1]
        instructions.append((direction, int(val)))
    else:
        x,y = l.split(',')
        points.add((int(x), int(y)))

for direction, val in instructions:
    new_points = set()
    for x, y in points:
        new_point = (x, y)
        if direction == 'y':
            if y > val:
                new_point = (x, 2 * val - y)
        else:
            if x > val:
                new_point = (2 * val - x, y)
        new_points.add(new_point)
    points = new_points
    break

print(len(points))
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')