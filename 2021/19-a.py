from utils import load_input
a = load_input(__file__)

from time import perf_counter
from collections import deque
t0 = perf_counter()
    
rots = [
    [ 1, 0, 0, 1], # 0 Degrees
    [ 0,-1, 1, 0], # 90 Degrees
    [-1, 0, 0,-1], # 180 Degrees
    [ 0, 1,-1, 0]  # 270 Degrees
]

def rotate(scanner, axis, rot):
    matrix = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    if axis[0] != 0:
        matrix[0][0] = axis[0]
        matrix[1][1] = rots[rot][0]
        matrix[1][2] = rots[rot][1]
        matrix[2][1] = rots[rot][2]
        matrix[2][2] = rots[rot][3]
    elif axis[1] != 0:
        matrix[0][0] = rots[rot][0]
        matrix[0][2] = rots[rot][1]
        matrix[1][1] = axis[1]
        matrix[2][0] = rots[rot][2]
        matrix[2][2] = rots[rot][3]
    elif axis[2] != 0:
        matrix[0][0] = rots[rot][0]
        matrix[0][1] = rots[rot][1]
        matrix[1][0] = rots[rot][2]
        matrix[1][1] = rots[rot][3]
        matrix[2][2] = axis[2]
    
    return [
        [beacon[0] * row[0] + beacon[1] * row[1] + beacon[2] * row[2] for row in matrix]
        for beacon in scanner
    ]
    
cube_faces = [
    (0, 1, 0, 0), # No rot
    (0, 1, 0, 1), # Move -z to point x
    (0, 1, 0, 2), # Move -x to point x
    (0, 1, 0, 3), # Move -x to point x
    (0, 0, 1, 1), # Move y to point x
    (0, 0, 1, 3), # Move -y to point x
]

scanners = []
current_scanner = []
if a[-1] != "":
    a.append("")
for l in a:
    if l == "":
        scanners.append(current_scanner)
        current_scanner = []
        continue
    if "---" in l:
        continue
    x,y,z = l.split(',')
    current_scanner.append([int(x), int(y), int(z)])

known_beacons = set([(x,y,z) for x,y,z in scanners[0]])
NEEDED_MATCHES = 12
def matches_known_beacons(scanner):
    for x_1, y_1, z_1 in known_beacons:
        for x_base , y_base, z_base in scanner[:-NEEDED_MATCHES]:
            x_d = x_1 - x_base
            y_d = y_1 - y_base
            z_d = z_1 - z_base
            beacon_count = 0
            for x_2, y_2, z_2 in scanner:
                x_new = x_2 + x_d
                y_new = y_2 + y_d
                z_new = z_2 + z_d
                if (x_new, y_new, z_new) in known_beacons:
                    beacon_count += 1
                    if beacon_count >= NEEDED_MATCHES:
                        return (x_d, y_d, z_d)
    return None
    
scanner_queue = deque([(str(i), scanners[i]) for i in range(1, len(scanners))])

while len(scanner_queue) > 0:
    index, scanner = scanner_queue.popleft()
    for x,y,z,r in cube_faces:
        scanner_rot = rotate(scanner, (x,y,z), r)
        for rot in range(4):
            current_check = rotate(scanner_rot, (1,0,0), rot)
            adjustment = matches_known_beacons(current_check)
            if adjustment is None:
                continue
            x_d, y_d, z_d = adjustment
            for x,y,z in current_check:
                x_new = x + x_d
                y_new = y + y_d
                z_new = z + z_d
                known_beacons.add((x_new, y_new, z_new))
            break
        else:
            continue
        break
    else:
        scanner_queue.append((index, scanner))

print(len(known_beacons))
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')