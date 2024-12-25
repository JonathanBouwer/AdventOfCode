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
            
            sides = set()
           
            if ny > 0 and a[ny-1][nx] == val:
                flood.append((nx,ny-1))
            else:
                sides.add("T")
    
            if nx > 0 and a[ny][nx-1] == val:
                flood.append((nx-1,ny))
            else:
                sides.add("L")

            if ny < len(a)-1 and a[ny+1][nx] == val:
                flood.append((nx,ny+1))
            else:
                sides.add("B")
            
            if nx < len(a[0])-1 and a[ny][nx+1] == val:
                flood.append((nx+1,ny))
            else:
                sides.add("R")

            vertex_count = 0
    
            if len(sides) == 4:
                # 4 vertices
                vertex_count += 4
            elif len(sides) == 3:
                # 3 vertices
                vertex_count += 2
            elif len(sides) == 2:
                # 0 vertices
                if "T" in sides and "B" in sides:
                    continue
                if "R" in sides and "L" in sides:
                    continue
                
                # Else
                # First vertex (TL, TR, BL, BR)
                vertex_count += 1
                
                # 1 Possible reflex angle vertex
                if "T" in sides and "L" in sides:
                    if a[ny+1][nx+1] != val:
                        vertex_count += 1
                elif "T" in sides and "R" in sides:
                    if a[ny+1][nx-1] != val:
                        vertex_count += 1
                elif "B" in sides and "L" in sides:
                    if a[ny-1][nx+1] != val:
                        vertex_count += 1
                elif "B" in sides and "R" in sides:
                    if a[ny-1][nx-1] != val:
                        vertex_count += 1
            elif len(sides) == 1:
                # 2 Possible reflex angle vertices
                if "T" in sides or "L" in sides:
                    if a[ny+1][nx+1] != val:
                        vertex_count += 1
                if "T" in sides or "R" in sides:
                    if a[ny+1][nx-1] != val:
                        vertex_count += 1
                if "B" in sides or "L" in sides:
                    if a[ny-1][nx+1] != val:
                        vertex_count += 1
                if "B" in sides or "R" in sides:
                    if a[ny-1][nx-1] != val:
                        vertex_count += 1
            elif len(sides) == 0:
                # 4 Possible reflex angle vertices
                if a[ny+1][nx+1] != val:
                    vertex_count += 1
                if a[ny+1][nx-1] != val:
                    vertex_count += 1
                if a[ny-1][nx+1] != val:
                    vertex_count += 1
                if a[ny-1][nx-1] != val:
                    vertex_count += 1
    
            perim += vertex_count # (F=V-E+2, F=2 on a 2D plane thus V=E)
            
        areas.append((val,area,perim))

total= 0
for v,q,w in areas:
    total += q*w
   
print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')