from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def parse_literal(bin_string):
    raw_literal = ""
    step = 0
    while True:
        raw_literal += bin_string[step+1:step+5]
        if bin_string[step] == "0":
            break
        step += 5
    return (int(raw_literal, 2), step+5)

def operate(type_id, val_1, val2):
    if type_id == 0:
        return val_1 + val2
    elif type_id == 1:
        return val_1 * val2
    elif type_id == 2:
        return min(val_1, val2)
    elif type_id == 3:
        return max(val_1, val2)
    elif type_id == 5:
        return 1 if val_1 > val2 else 0
    elif type_id == 6:
        return 1 if val_1 < val2 else 0
    elif type_id == 7:
        return 1 if val_1 == val2 else 0

def parse_bin(bin_string):
    version = int(bin_string[0:3], 2)
    type_id = int(bin_string[3:6], 2)
    bin_string = bin_string[6:]
    result = -1
    consumed = 6
    
    if type_id == 4:
        result, c = parse_literal(bin_string)
        consumed += c
    else:
        length_type_id = int(bin_string[0], 2)
        bin_string = bin_string[1:]
        consumed += 1
        vals = []
        
        if length_type_id == 0:
            length = int(bin_string[:15], 2)
            bin_string = bin_string[15:]
            seen = 0
            while seen < length:
                t, c = parse_bin(bin_string[seen:length])
                vals.append(t)
                seen += c
            consumed += 15 + length
        elif length_type_id == 1:
            subpackets = int(bin_string[:11], 2)
            bin_string = bin_string[11:]
            consumed = 6 + 1 + 11
            for i in range(subpackets):
                t, c = parse_bin(bin_string)
                vals.append(t)
                consumed += c
                bin_string = bin_string[c:]

        result = vals[0]
        for val in vals[1:]:
            result = operate(type_id, result, val)

    return (result, consumed)

a = a[0]
base_bin_string = f"{int('F'+a, 16):b}"[4:]
print(parse_bin(base_bin_string)[0])

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')