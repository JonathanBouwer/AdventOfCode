from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

gates = {}

init = True
instructions = []
for l in a:
    if l == "":
        init = False
        continue
    
    if init:
        k,v = l.split(": ")
        gates[k] = int(v)
    else:
        i1, op, i2, dash, o1 = l.split(" ")
        instructions.append((i1, op, i2, o1))
        
while len(instructions) > 0:
    i1, op, i2, o1 = instructions.pop(0)
    if i1 in gates and i2 in gates:
        if op == "AND":
            gates[o1] = gates[i1] & gates[i2]
        elif op == "OR":
            gates[o1] = gates[i1] | gates[i2]
        elif op == "XOR":
            gates[o1] = gates[i1] ^ gates[i2]
    else:
        instructions.append((i1, op, i2, o1))

z = []
for k, v in sorted(gates.items()):
    if k[0] == "z":
        z.append(str(v))

z = reversed(z)
print(int("".join(z), 2))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')