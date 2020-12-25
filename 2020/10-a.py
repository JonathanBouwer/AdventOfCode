from time import time
t0 = time()

a = [
26,
97,
31,
7,
2,
10,
46,
38,
112,
54,
30,
93,
18,
111,
29,
75,
139,
23,
132,
85,
78,
99,
8,
113,
87,
57,
133,
41,
104,
98,
58,
90,
13,
91,
20,
68,
103,
127,
105,
114,
138,
126,
67,
32,
145,
115,
16,
141,
1,
73,
45,
119,
51,
40,
35,
150,
118,
53,
80,
79,
65,
135,
74,
47,
128,
64,
17,
4,
84,
83,
147,
142,
146,
9,
125,
94,
140,
131,
134,
92,
66,
122,
19,
86,
50,
52,
108,
100,
71,
61,
44,
39,
3,
72
]

a.append(max(a)+3)
a = sorted(a)

diffs = {1: 0, 3: 0}
prev = 0
for val in a:
    diffs[val - prev] += 1
    prev = val
    
print(f"{diffs[1] * diffs[3]}")

print(f'Time: {(time()-t0) * 1000}ms')