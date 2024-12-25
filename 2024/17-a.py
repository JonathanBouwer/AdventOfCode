from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

reg_a = int(a[0].split(" ")[-1])
reg_b = int(a[1].split(" ")[-1])
reg_c = int(a[2].split(" ")[-1])
instructions = [int(x) for x in a[4].split(" ")[1].split(",")]
pc = 0

output = []
while pc < len(instructions):
    op_code = instructions[pc]
    operand = instructions[pc+1]
    
    cmb_operand = operand
    if operand == 4:
        cmb_operand = reg_a
    elif operand == 5:
        cmb_operand = reg_b
    elif operand == 6:
        cmb_operand = reg_c
    
    if op_code == 0: #adv
        reg_a = reg_a // (2**cmb_operand) # fail if reg_a negative
    elif op_code == 1: #bxl
        reg_b = reg_b ^ operand
    elif op_code == 2: #bst
        reg_b = cmb_operand % 8
    elif op_code == 3: #jnz
        if reg_a != 0:
            pc = operand
            continue
    elif op_code == 4: #bxc
        reg_b = reg_b ^ reg_c
    elif op_code == 5: #out
        output.append(cmb_operand%8)
    elif op_code == 6: #bdv
        reg_b = reg_a // (2**cmb_operand) # fail if reg_b negative
    elif op_code == 7: #cdv
        reg_c = reg_a // (2**cmb_operand) # fail if reg_c negative

    pc += 2

print(",".join(str(x) for x in output))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')