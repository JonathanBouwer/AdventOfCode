from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

robots = []
seconds = 100
lx = 101
ly = 103
for l in a:
    p, v = l.split(" ")
    px = int(p.split("p=")[1].split(",")[0])
    py = int(p.split(",")[1])
    vx = int(v.split("v=")[1].split(",")[0])
    vy = int(v.split(",")[1])
    robots.append(((px+seconds*vx)%lx, (py+seconds*vy)%ly))
    
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for r in robots:
    x,y = r
    if x < lx // 2 and y < ly // 2:
        q1 += 1
    elif x > lx // 2 and y < ly // 2:
        q2 += 1
    elif x < lx // 2 and y > ly // 2:
        q3 += 1
    elif x > lx // 2 and y > ly // 2:
        q4 += 1

print(q1*q2*q3*q4)
    
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')