from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

import os
import time

robots = []
lx = 101
ly = 103
for l in a:
    p, v = l.split(" ")
    px = int(p.split("p=")[1].split(",")[0])
    py = int(p.split(",")[1])
    vx = int(v.split("v=")[1].split(",")[0])
    vy = int(v.split(",")[1])
    robots.append((px,py,vx,vy))

# Christmas tree pattern contains sequences of many single robots next to each other
dense_threshold = 30
for second in range(10000):
    row_counts = [0 for j in range(ly)]
    for robot in robots:
        row_counts[robot[1]] += 1

    has_dense_row = False
    for row_count in row_counts:
        if row_count > dense_threshold:
            has_dense_row = True
            break
            
    found = False
    if has_dense_row:
        output = [[0 for i in range(lx)] for j in range(ly)]
        for robot in robots:
            x,y,vx,vy = robot
            output[y][x] += 1
        
        for y in range(ly):
            if row_counts[y] < dense_threshold:
                continue
                
            longest_ones = 0
            current_ones = 0
            for x in output[y]:
                if x == 1:
                    current_ones += 1
                else:
                    longest_ones = max(longest_ones, current_ones)
                    current_ones = 0
                    

            if longest_ones > dense_threshold:
                print(second)
                found = True
                # for l in output:
                    # print("".join(["." if x == 0 else str(x) for x in l]))
                break
    
    if found:
        break

    robots = [((x+vx)%lx,(y+vy)%ly,vx,vy) for x,y,vx,vy in robots]
    
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')