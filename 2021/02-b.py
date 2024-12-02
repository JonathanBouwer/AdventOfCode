from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

x = 0
y = 0
aim = 0
for i in a:
    instruction, val = i.split(' ')
    amount = int(val)
    if instruction == 'forward':
        x+=amount
        y+=aim*amount
    elif instruction == 'up':
        aim-=amount
    elif instruction == 'down':
        aim+=amount

print(x*y)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')