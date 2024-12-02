from time import perf_counter
t0 = perf_counter()

max_cup = 1000000
a = [int(i) for i in "963275481"]

circle = [i + 1 for i in range(max_cup + 1)]
circle[0] = max_cup + 1 # Out of range, should never be called
for i in range(len(a) - 1):
    cur_val = a[i]
    next_val = a[i + 1]
    circle[cur_val] = next_val

circle[a[-1]] = 10
circle[max_cup] = a[0]

current_cup = a[0]

for i in range(10000000):
    rem_cup_1 = circle[current_cup];
    rem_cup_2 = circle[rem_cup_1];
    rem_cup_3 = circle[rem_cup_2];
    circle[current_cup] = circle[rem_cup_3]

    dest_cup = current_cup - 1
    while True:
        if dest_cup <= 0:
            dest_cup = max_cup
        if dest_cup != rem_cup_1 and dest_cup != rem_cup_2 and dest_cup != rem_cup_3:
            break
        dest_cup -= 1
    
    old_next = circle[dest_cup]
    circle[dest_cup] = rem_cup_1
    circle[rem_cup_3] = old_next
    
    current_cup = circle[current_cup]

print(circle[1] * circle[circle[1]])

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')