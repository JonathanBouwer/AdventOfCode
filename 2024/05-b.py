from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

from functools import cmp_to_key

rules = [x for x in a if "|" in x]
updates = [x for x in a if "|" not in x][1:]

comp_dict = {}
for rule in rules:
    v,k = rule.split("|")
    if k not in comp_dict:
        comp_dict[k] = set()
    comp_dict[k].add(v)

def compare(p1, p2):
    if p2 in comp_dict and p1 in comp_dict[p2]:
        return -1
    if p1 in comp_dict and p2 in comp_dict[p1]:
        return 1
    return 0

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
        continue
    sorted_pages = sorted(pages, key=cmp_to_key(compare))
    total += int(sorted_pages[len(sorted_pages)//2])

print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')