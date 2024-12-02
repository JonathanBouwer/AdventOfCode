from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

raise Exception("Incomplete")

cubes = []
for l in a:
    setting,cuboid = l.split(" ")
    xr,yr,zr = cuboid.split(",")
    xmin,xmax=xr.split('..')
    xmin=xmin[2:]
    xmin = int(xmin)
    xmax = int(xmax)
    ymin,ymax=yr.split('..')
    ymin=ymin[2:]
    ymin = int(ymin)
    ymax = int(ymax)
    zmin,zmax=zr.split('..')
    zmin=zmin[2:]
    zmin = int(zmin)
    zmax = int(zmax)
    cubes.append((setting,(xmin,xmax,ymin,ymax,zmin,zmax)))

engine = set()
cube_index = 0
while cube_index < len(cubes):
    print(len(cubes) - cube_index)
    setting, cube = cubes[cube_index]
    cube_index += 1
    xmin,xmax,ymin,ymax,zmin,zmax = cube
    if setting == "on":
        outside_all_cubes = True
        inside_another_cube = False
        cubes_within = []
        for x1,x2,y1,y2,z1,z2 in engine:
            if outside_all_cubes: # Check if outside this cube
                if not ((xmax < x1 or xmin > x2) and (ymax < y1 or ymin > y2) and (zmax < z1 or zmin > z2)):
                    outside_all_cubes = False
            
            if xmax <= x2 and xmin >= x1 and ymax <= y2 and ymin >= y1 and zmax <= z2 and zmin >= z1:
                inside_another_cube = True
                break
                
            if xmax >= x2 and xmin <= x1 and ymax >= y2 and ymin <= y1 and zmax >= z2 and zmin <= z1:
                cubes_within.append((x1,x2,y1,y2,z1,z2))
            
        if len(cubes_within) > 0 and inside_another_cube:
            raise Exception("What Happened")
            
        if inside_another_cube:
            #print("INSIDE")
            continue
            
        if outside_all_cubes:
            #print("OUTSIDE")
            engine.add((xmin,xmax,ymin,ymax,zmin,zmax))
            
        if len(cubes_within) > 0:
            for cube in cubes_within:
                #print("DROP", cube)
                engine.remove(cube)
            cubes.append((setting, (xmin,xmax,ymin,ymax,zmin,zmax)))
            continue
            
        if outside_all_cubes:
            continue
            
        for x1,x2,y1,y2,z1,z2 in engine:
            if (xmax < x1 or xmin > x2) and (ymax < y1 or ymin > y2) and (zmax < z1 or zmin > z2):
                continue
        
            ix1 = max(x1,xmin)
            ix2 = min(x2,xmax)
            iy1 = max(y1,ymin)
            iy2 = min(y2,ymax)
            iz1 = max(z1,zmin)
            iz2 = min(z2,zmax)
            
            if ix1 > xmin:
                cubes.append((setting, (xmin,ix1-1,ymin,ymax,zmin,zmax)))
            if ix2 < xmax:
                cubes.append((setting, (ix2+1,xmax,ymin,ymax,zmin,zmax)))
            if iy1 > ymin:
                cubes.append((setting, (ix1,ix2,ymin,iy1-1,zmin,zmax)))
            if iy2 < ymax:
                cubes.append((setting, (ix1,ix2,iy2+1,ymax,zmin,zmax)))
            if iz1 > zmin:
                cubes.append((setting, (ix1,ix2,iy1,iy2,zmin,iz1-1)))
            if iy2 < ymax:
                cubes.append((setting, (ix1,ix2,iy1,iy2,iz2+1,zmax)))
            break
        else:
            print(engine)
            print((xmin,xmax,ymin,ymax,zmin,zmax))
            raise Exception("NEVER INTERSECTED")
    else:
        pass
        #print("OFF")
        

print(engine)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')