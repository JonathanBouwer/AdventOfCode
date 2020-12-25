from time import time
t0 = time()

t = 1000510

a = [19,41,523,17,13,29,853,37,23]

min_wait = max(a) + 1
min_route = -1
for val in a:
    if val - (t % val) < min_wait:
        min_wait = val - (t % val)
        min_route = val

print(min_route * min_wait)

print(f'Time: {(time()-t0) * 1000}ms')