from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def add_left(data, val):
    if isinstance(data,int):
        return data + val
    l, r = data
    return (add_left(l, val), r)

def add_right(data, val):
    if isinstance(data,int):
        return data + val
    l, r = data
    return (l, add_right(r, val))

def explode(data, depth):
    if isinstance(data,int):
        return data, 0, 0, False
    l, r = data

    result_l, out_add_left, a_r, x = explode(l, depth+1)
    if a_r > 0:
        r = add_left(r, a_r)
    if x:
        return (result_l, r), out_add_left, 0, x

    result_r, a_l, out_add_right, x = explode(r, depth+1)
    if a_l > 0:
        result_l = add_right(result_l, a_l)
    if x:
        return (result_l, result_r), out_add_left, out_add_right, x

    if depth >= 4:
        return 0, result_l, result_r, True
    return (result_l, result_r), out_add_left, out_add_right, False

def split(data):
    if isinstance(data,int):
        if data >= 10:
            t = data // 2
            return (t, data - t), True
        return data, False
    l, r = data
    result_l, cont_l = split(l)
    if cont_l:
        return (result_l, r), cont_l
    result_r, cont_r = split(r)
    return (result_l, result_r), cont_r

def simplify(data):
    res = data
    should_continue = True
    while should_continue:
        res, a_l, a_r, x = explode(res, 0)
        if x:
            continue
        res, should_continue = split(res)
    return res

def magnitude(data):
    if isinstance(data,int):
        return data
    l, r = data
    return 3 * magnitude(l) + 2 * magnitude(r)

lines = [eval(x) for x in a]
best = -1
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        val = magnitude(simplify((lines[i], lines[j])))
        if val > best:
            best = val
    
print(best)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')