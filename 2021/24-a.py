from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

OP_NOP = -1
OP_INP = 0
OP_ADD = 1
OP_MUL = 2
OP_DIV = 3
OP_MOD = 4
OP_EQL = 5
OP_NEQ = 6
OP_SET = 7
op_names = ["OP_INP", "OP_ADD", "OP_MUL", "OP_DIV", "OP_MOD", "OP_EQL", "OP_NEQ", "OP_SET"]

program = []
def compile():
    tc = perf_counter()
    reg = {"w": 0, "x": 0, "y": 0, "z": 0}
    prev_inst = {"w": None, "x": None, "y": None, "z": None}
    for l in a:
        if l[0] == "i":
            step = (OP_INP, l[4], "", False)
            program.append(step)
            prev_inst[l[4]] = step
            reg[l[4]] = None
            continue

        op, v1, v2 = l.split(" ")
        op = op[1]
        lookup = False
        lookup_val = None
        if v2 in ["w", "x", "y", "z"]:
            lookup_val = reg[v2]
            if lookup_val is not None:
                v2 = lookup_val
            else:
                lookup = True
                prev_inst[v2] = None
        else:
            v2 = int(v2)
        
        # Parse OP
        if op == "d":
            inst = OP_ADD
        elif op == "u":
            inst = OP_MUL
        elif op == "i":
            inst = OP_DIV
        elif op == "o":
            inst = OP_MOD
        elif op == "q":
            inst = OP_EQL
        else:
            raise Exception()
        
        # Reg Constants
        new_reg_val = None
        if not lookup:
            if reg[v1] != None:
                if inst == OP_ADD:
                    new_reg_val = reg[v1] + v2
                elif inst == OP_MUL:
                    new_reg_val = reg[v1] * v2
                elif inst == OP_DIV:
                    new_reg_val = reg[v1] // v2
                elif inst == OP_MOD:
                    new_reg_val = reg[v1] % v2
                elif inst == OP_EQL:
                    new_reg_val = 1 if reg[v1] == v2 else 0
            else:
                if inst == OP_MUL and v2 == 0:
                    new_reg_val = 0
        
        # Check SET
        if inst == OP_ADD:
            if reg[v1] == 0:
                inst = OP_SET
        elif inst == OP_MUL:
            if reg[v1] == 1:
                inst = OP_SET
                
        if inst == OP_SET:
            if reg[v1] == v2:
                inst = OP_NOP

        reg[v1] = new_reg_val
        
        # Check NOP
        if inst == OP_ADD:
            if v2 == 0:
                inst = OP_NOP
        elif inst == OP_MUL:
            if v2 == 1:
                inst = OP_NOP
            elif reg[v1] == 0:
                inst = OP_NOP
        elif inst == OP_DIV:
            if v2 == 1:
                inst = OP_NOP
            elif reg[v1] == 0:
                inst = OP_NOP
        elif inst == OP_MOD:
            if v2 == 1:
                inst = OP_NOP
            elif reg[v1] == 0:
                inst = OP_NOP
                
        # Check Prev
        if inst == OP_EQL:
            prev = prev_inst[v1]
            if prev is not None and prev[0] == OP_EQL and v2 == 0:
                i = len(program)
                while True:
                    i -= 1
                    cur_step = program[i]
                    if cur_step == prev:
                        program[i] = (OP_NEQ, cur_step[1], cur_step[2], cur_step[3])
                        inst = OP_NOP
                        break

        if inst != OP_NOP:
            step = (inst, v1, v2, lookup)
            program.append(step)
            prev_inst[v1] = step
            # print(reg)
    print(f'Compilation took: {(perf_counter()-tc) * 1000:.3f}ms')

    for l in program[:50]:
        if l[0] == 0:
            print()
        print((op_names[l[0]], l[1], l[2], l[3]))
    print(len(program), len(a))
    counts = {}
    for l in program:
        op = op_names[l[0]]
        if op not in counts:
            counts[op] = 0
        counts[op] += 1
    print(counts)
    # raise Exception("Incomplete")

times = []
max_time = 0
def func(input_val):
    global max_time
    t1 = perf_counter()
    data = [int(x) for x in input_val]
    index = 0
    reg = {"w": 0, "x": 0, "y": 0, "z": 0}
    for inst, v1, v2, lookup in program:
        print(op_names[inst], v1, f"{v2: <2}", reg)
        if inst == OP_INP:
            reg[v1] = data[index]
            index += 1
            continue

        if lookup:
            v2 = reg[v2]

        if inst == OP_ADD:
            reg[v1] += v2
        elif inst == OP_SET:
            reg[v1] = v2
        elif inst == OP_MUL:
            reg[v1] *= v2
        elif inst == OP_MOD:
            reg[v1] %= v2
        elif inst == OP_DIV:
            reg[v1] //= v2
        elif inst == OP_NEQ:
            reg[v1] = 0 if reg[v1] == v2 else 1
        else:
            raise Exception("No path for " + inst)

    times.append((perf_counter() - t1) * 1000)
    if times[-1] > max_time:
        max_time = times[-1]
        print(input_val)
    return reg["z"] == 0

compile()
print(func("11711111787111"))
if False:
    from random import randrange
    for i in range(10**15-1, 10**15-10**5, -1):
        v = f"{i}"
        if "0" in v:
            continue
        if func(v):
            print(v)

times.sort()
print("min", times[0])
print("p50", times[(50 * len(times)) // 100])
print("p90", times[(90 * len(times)) // 100])
print("p99", times[(99 * len(times)) // 100])
print("max", times[-1])

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')