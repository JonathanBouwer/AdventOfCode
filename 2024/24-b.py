from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

map = {}
init = True
z_regs = []
base_xors = {}
for l in a:
    if l == "":
        init = False
        continue
    
    if not init:
        i1, op, i2, dash, o1 = l.split(" ")
        map[o1] = (i1, op, i2)
        if o1[0] == "z":
            z_regs.append(o1)
        if op == "XOR" and i1[0] in "xy" and i2[0] in "xy" and i1[1:] == i2[1:]:
            base_xors[int(i1[1:])] = o1

# Initially solved by hand by examining input and output, turned that algorithm into below code
# print("dnt,gdf,gwc,jst,mcm,z05,z15,z30")

swaps = []
# The algorithm for addition with carry is
# zn = (xn XOR yn) XOR (carry from z(n-1))
for i, reg in enumerate(sorted(z_regs)):
    # For each z register we check if it's an XOR including the correct base xor, otherwise we swap
    i1, op, i2 = map[reg]
    if i >= len(base_xors):
        break
    expected_xor = base_xors[i] if i > 0 else "x00"
    if op != "XOR" or (i1 != expected_xor and i2 != expected_xor):
        # Search for the register which is XORing with the expected xor
        for k, v in map.items():
            pi1, pop, pi2 = v
            if pop == "XOR" and (pi1 == expected_xor or pi2 == expected_xor):
                map[reg] = (pi1, pop, pi2)
                map[k] = (i1, op, i2)
                swaps.append(k)
                swaps.append(reg)
                break
        else:
            if op != "XOR":
                print("I'M VERY CONFUSED")
                
            # If you can't find it, that means one of the 2 values you are XORing must be wrong
            # One of the XORs should be the base, the other should be an OR
            qreg1 = i1
            qreg2 = i2
            q1i1, q1op, q1i2 = map[qreg1]
            q2i1, q2op, q2i2 = map[qreg2]
            xi1, xop, xi2 = map[expected_xor]
            if q1op == "AND": # XOR and OR are okay, AND is bad so we need to swap it with the expected base
                map[expected_xor] = (q1i1, q1op, q1i2)
                map[qreg1] = (xi1, xop, xi2)
                swaps.append(expected_xor)
                swaps.append(qreg1)
            elif q2op == "AND":
                map[expected_xor] = (q2i1, q2op, q2i2)
                map[qreg2] = (xi1, xop, xi2)
                swaps.append(expected_xor)
                swaps.append(qreg2)
            else:
                print("I'M CONFUSED")
         
print(",".join(sorted(swaps)))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')