from utils import load_input
a = load_input(__file__)[0]

from time import perf_counter
t0 = perf_counter()

posistions = [int(x) for x in a.split(',')]
low = min(posistions)
high = max(posistions)

def calc_fuel(i):
    fuel = 0
    for pos in posistions:
        dist = abs(pos - i)
        fuel += dist * (dist + 1) // 2
    return fuel

bottom_fuel = calc_fuel(low)

while low < high - 2:
    inc = (high - low) // 3
    mid_1 = low + inc
    mid_2 = high - inc
    fuel_1 = calc_fuel(mid_1)
    fuel_2 = calc_fuel(mid_2)
    if bottom_fuel > fuel_1 and fuel_2 > fuel_1:
        high = mid_2
    else:
        low = mid_1
        bottom_fuel = fuel_1

lowest_fuel = bottom_fuel
lowest_pos = low
for i in range(low, high):
    fuel = calc_fuel(i)
    if fuel < lowest_fuel:
        lowest_fuel = fuel
        lowest_pos = i

print(lowest_pos, lowest_fuel)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')