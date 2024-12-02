from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

points = set()
instructions = []
is_points = True
for l in a:
    if l == '':
        is_points = False
        continue
    if is_points:
        x, y = l.split(',')
        points.add((int(x), int(y)))
    else:
        inst, val = l.split('=')
        direction = inst.split(' ')[-1]
        instructions.append((direction, int(val)))

for direction, val in instructions:
    new_points = set()
    for x, y in points:
        new_point = (x, y)
        if direction == 'y':
            if y > val:
                new_point = (x, 2 * val - y)
        if direction == 'x':
            if x > val:
                new_point = (2 * val - x, y)
        new_points.add(new_point)
    points = new_points
    
max_x = -1
max_y = -1
for x, y in points:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

output = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]

for x, y in points:
    output[y][x] = '#'
    
for row in output:
    print(''.join(row))    

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')