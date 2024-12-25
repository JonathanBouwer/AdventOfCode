from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

areas = []

seen = set()
for y in range(len(a)):
    for x in range(len(a[y])):
        if (x,y) in seen:
            continue
       
        flood = [(x,y)]
        perim = 0
        area = 0
        val = a[y][x]
        while len(flood) > 0:
            nx,ny = flood.pop(0)
            if (nx,ny) in seen:
                continue
            seen.add((nx,ny))
            area += 1
           
            if ny > 0 and a[ny-1][nx] == val:
                flood.append((nx,ny-1))
            else:
                perim += 1
           
            if nx > 0 and a[ny][nx-1] == val:
                flood.append((nx-1,ny))
            else:
                perim += 1
           
            if ny < len(a)-1 and a[ny+1][nx] == val:
                flood.append((nx,ny+1))
            else:
                perim += 1
           
            if nx < len(a[0])-1 and a[ny][nx+1] == val:
                flood.append((nx+1,ny))
            else:
                perim += 1

        areas.append((val,area,perim))

total= 0
for v,q,w in areas:
    total += q*w
   
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')