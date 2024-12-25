from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

count =  0
for l in a:
    levels = [int(x) for x in l.split(" ")]
    is_inc = False
    for x in range(len(levels) - 1):
        if x == 0 and len(levels) >= 2 and levels[0] < levels[1]:
            is_inc = True

        if abs(levels[x] - levels[x+1]) == 0:
            break
        
        if abs(levels[x] - levels[x+1]) > 3:
            break
            
        if is_inc:
            if levels[x] > levels[x+1]:
                break
        else:
            if levels[x] < levels[x+1]:
                break
    else:
        count += 1 

print(count)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')