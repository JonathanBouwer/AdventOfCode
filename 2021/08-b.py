from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter() 

inputs = [{
    'input_digits': x.split('|')[0][:-1].split(' '),
    'output_digits': x.split('|')[1][1:].split(' ')
} for x in a]

#  000
# 1   2
# 1   2
# 1   2
#  333
# 4   5
# 4   5
# 4   5
#  666

digit_map = {
    1: set([2,5]),
    2: set([0,2,3,4,6]),
    3: set([0,2,3,5,6]),
    4: set([1,2,3,5]),
    5: set([0,1,3,5,6]),
    6: set([0,1,3,4,5,6]),
    7: set([0,2,5]),
    8: set([0,1,2,3,4,5,6]),
    9: set([0,1,2,3,5,6]),
    0: set([0,1,2,4,5,6])
}

total = 0
for input_obj in inputs:
    input_val = input_obj['input_digits']
    segments = {i: set() for i in range(7)}
    segments[4] = set(['a','b','c','d','e','f','g'])
    segments[6] = set(['a','b','c','d','e','f','g'])

    for digit in input_val:
        digit_len = len(digit)
        if digit_len == 2:    # 1
            chars = [c for c in digit]
            segments[2].update(chars)
            segments[5].update(chars)
        elif digit_len == 3:  # 7
            segments[0].update([c for c in digit])
        elif digit_len == 4:  # 4
            chars = [c for c in digit]
            segments[1].update(chars)
            segments[3].update(chars)
    
    known_discard_groups = [
        [2, 5], # 1 digit
        [0],    # 7 digit
        [1, 3]  # 4 digit
    ]

    for discard_group in known_discard_groups:
        for i in range(7):
            if i in discard_group:
                continue
            for c in segments[discard_group[0]]:
                segments[i].discard(c)
            
    intersections = [ # length, seg, alt
        (6, 3, 1), # Identify missing segment 3 in 0 digit
        (6, 2, 5), # Identify missing segment 2 in 6 digit
        (5, 4, 6)  # Identify missing segment 4 in 9 digit
    ]

    for length, seg, alt in intersections:
        for digit in input_val:
            if len(digit) != length:
                continue

            for c in segments[seg]:
                if c not in digit:
                    for ch in digit:
                        segments[seg].discard(ch)
                    break
            else:
                continue
            break
                
        for c in segments[seg]:
            segments[alt].discard(c)
    
    invert_mapping = {}
    for key, val in segments.items():
        for c in val:
            if c is not None:
                invert_mapping[c] = key
                break
    
    output_val = ''
    for digit in input_obj['output_digits']:
        output_set = set([invert_mapping[c] for c in digit])
        for key, segment_set in digit_map.items():
            if segment_set == output_set:
                output_val = output_val + str(key)
                break
    total += int(output_val)

print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')