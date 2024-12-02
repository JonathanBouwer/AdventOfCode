from time import perf_counter
t0 = perf_counter()

p1 = [
26,
14,
6,
34,
37,
9,
17,
39,
4,
5,
1,
8,
49,
16,
18,
47,
20,
31,
23,
19,
35,
41,
28,
15,
44
]

p2 = [
7,
2,
10,
25,
29,
46,
40,
45,
11,
50,
42,
24,
38,
13,
36,
22,
33,
3,
43,
21,
48,
30,
32,
12,
27
]

while len(p1) > 0 and len(p2) > 0:
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    if p1_card > p2_card:
        p1.append(p1_card)
        p1.append(p2_card)
    else:
        p2.append(p2_card)
        p2.append(p1_card)
        
p1_score = sum([a * (len(p1) - i) for i, a in enumerate(p1)])
p2_score = sum([a * (len(p2) - i) for i, a in enumerate(p2)])
print(max(p1_score, p2_score))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')