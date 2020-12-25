from time import time
from math import sqrt
t0 = time()

card_public_key = 335121
door_public_key = 363891
p = 20201227
m = 7

# Big Step Little Step Algorithm
sqrt_p = int(sqrt(p)) + 1
S = pow(m, -1, p) ** sqrt_p

col_1 = [1]
col_2 = [door_public_key]
set_col_1 = {1}
for i in range(1, sqrt_p):
    col_1.append(col_1[i-1] * m % p)
    set_col_1.add(col_1[i])
    col_2.append(col_2[i-1] * S % p)
    if col_2[i] in set_col_1:
        break
    
for i_1, v_1 in enumerate(col_1):
    for i_2, v_2 in enumerate(col_2):
        if v_1 == v_2:
            print(pow(card_public_key, i_1 + sqrt_p * i_2, p))
            break
    else:
        continue
    break

print(f'Time: {(time()-t0) * 1000}ms')