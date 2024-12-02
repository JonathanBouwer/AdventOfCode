from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

outputs = [x.split('|')[1][1:].split(' ') for x in a]

count = 0
for output in outputs:
    for digit in output:
        if len(digit) != 5 and len(digit) !=6:
            count += 1
            
print(count)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')