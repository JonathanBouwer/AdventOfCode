from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

alg = a[0]
a = a[2:]

NN = 50
BORDER = 2*NN
WIDTH = len(a[0])+2*BORDER
HEIGHT = len(a)+2*BORDER
data = [['.']*HEIGHT for i in range(HEIGHT)]
for i in range(0, len(a)):
    for j in range(0, len(a[0])):
        data[BORDER + i][BORDER + j] = a[i][j]

for n in range(NN):
    new_data = [['.']*WIDTH]
    for i in range(1, HEIGHT-1):
        new_row = ['.']*WIDTH
        for j in range(1, WIDTH-1):
            index = 0
            # Unroll loop for performance
            index *= 2
            if data[i-1][j-1] == '#':
                index += 1
            index *= 2
            if data[i-1][j] == '#':
                index += 1
            index *= 2
            if data[i-1][j+1] == '#':
                index += 1
            index *= 2
            if data[i][j-1] == '#':
                index += 1
            index *= 2
            if data[i][j] == '#':
                index += 1
            index *= 2
            if data[i][j+1] == '#':
                index += 1
            index *= 2
            if data[i+1][j-1] == '#':
                index += 1
            index *= 2
            if data[i+1][j] == '#':
                index += 1
            index *= 2
            if data[i+1][j+1] == '#':
                index += 1
            new_row[j] = alg[index]
        new_data.append(new_row)
    new_data.append(['.']*WIDTH)
    data = new_data

total = 0
for r in data[NN:-NN]:
    for c in r[NN:-NN]:
        if c == '#':
            total +=1
            
print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')