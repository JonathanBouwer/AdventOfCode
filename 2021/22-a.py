from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

REGION_MIN=-50
REGION_MAX=50

engine = set()
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
    
    if xmin < REGION_MIN or xmax > REGION_MAX or ymin < REGION_MIN or ymax > REGION_MAX or zmin < REGION_MIN or zmax > REGION_MAX:
        continue
        
    if setting == "on":
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                for z in range(zmin, zmax+1):
                    engine.add((x,y,z))
    else:
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                for z in range(zmin, zmax+1):
                    engine.discard((x,y,z))

print(len(engine))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')