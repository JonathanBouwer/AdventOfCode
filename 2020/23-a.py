from time import time
t0 = time()

max_cup = 9
a = [int(i) for i in "963275481"]

current_cup = 0

for i in range(100):
    #print("current cup position", current_cup)
    current_cup_val = a[current_cup]
    #print("cups:", a)
    removed_cups = []
    for i in range(3):
        removed_cups.append(a[(current_cup + 1 + i) % len(a)])
    #print("pick up:", removed_cups)
    a = [i for i in a if i not in removed_cups]
    destination_cup = current_cup_val - 1
    while True:
        if destination_cup <= 0:
            destination_cup = max_cup
        if destination_cup not in removed_cups:
            break
        destination_cup -= 1
    #print("destination:", destination_cup)
            
    dest_cup_pos = a.index(destination_cup)
    a = a[:dest_cup_pos + 1] + removed_cups + a[dest_cup_pos + 1:]
    current_cup = (a.index(current_cup_val) + 1) % len(a)
    #print()
    
    
#print("final:", a)
pos_1 = a.index(1)
a = a[pos_1:] + a[:pos_1]
print("".join([str(i) for i in a[1:]]))

print(f'Time: {(time()-t0) * 1000}ms')