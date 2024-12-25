from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

rules = [x for x in a if "|" in x]
updates = [x for x in a if "|" not in x][1:]

comp_dict = {}
for rule in rules:
    v,k = rule.split("|")
    if k not in comp_dict:
        comp_dict[k] = set()
    comp_dict[k].add(v)
    
total = 0
for update in updates:
    pages = update.split(",")
    for i in range(len(pages)):
        p1 = pages[i]
        if p1 not in comp_dict:
            continue
        rule = comp_dict[p1]
        for j in range(i, len(pages)):
            p2 = pages[j]
            if p2 in rule:
                # print("Invalid because {} comes after {}".format(p2, p1))
                break
        else:
            continue
        break
    else:
        # print("{} is valid".format(pages))
        total += int(pages[len(pages)//2])

print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')