from time import time
t0 = time()

a = [5,1,9,18,13,8,0]

n = 30000000

cache = [-1] * (n * 2)

for i, val in enumerate(a):
    cache[val * 2 + 1] = i + 1
    
cur = a[-1]
for i in range(len(a), n):
    cache[cur * 2] = cache[cur * 2 + 1]
    cache[cur * 2 + 1] = i
    cur = 0 if cache[cur * 2] == -1 else i - cache[cur * 2]

print(cur)

print(f'Time: {(time()-t0) * 1000}ms')
