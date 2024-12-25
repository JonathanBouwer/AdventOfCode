from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

numpad = {
    'A': {
        'A': 'A',
        '0': '<A',
        '1': '^<<A',
        '2': '^<A',
        '3': '^A',
        '4': '^^<<A',
        '5': '<^^A',
        '6': '^^A',
        '7': '^^^<<A',
        '8': '<^^^A',
        '9': '^^^A'
    },
    '0': {
        'A': '>A',
        '0': 'A',
        '1': '^<A',
        '2': '^A',
        '3': '^>A',
        '4': '^^<A',
        '5': '^^A',
        '6': '^^>A',
        '7': '^^^<A',
        '8': '^^^A',
        '9': '^^^>A'
    },
    '1': {
        'A': '>>vA',
        '0': '>vA',
        '1': 'A',
        '2': '>A',
        '3': '>>A',
        '4': '^A',
        '5': '^>A',
        '6': '^>>A',
        '7': '^^A',
        '8': '^^>A',
        '9': '^^>>A'
    },
    '2': {
        'A': '>vA',
        '0': 'vA',
        '1': '<A',
        '2': 'A',
        '3': '>A',
        '4': '^<A',
        '5': '^A',
        '6': '^>A',
        '7': '<^^A',
        '8': '^^A',
        '9': '^^>A'
    },
    '3': {
        'A': 'vA',
        '0': '<vA',
        '1': '<<A',
        '2': '<A',
        '3': 'A',
        '4': '<<^A',
        '5': '<^A',
        '6': '^A',
        '7': '<<^^A',
        '8': '<^^A',
        '9': '^^A'
    },
    '4': {
        'A': '>>vvA',
        '0': '>vvA',
        '1': 'vA',
        '2': 'v>A',
        '3': 'v>>A',
        '4': 'A',
        '5': '>A',
        '6': '>>A',
        '7': '^A',
        '8': '^>A',
        '9': '^>>A'
    },
    '5': {
        'A': 'vv>A',
        '0': 'vvA',
        '1': '<vA',
        '2': 'vA',
        '3': 'v>A',
        '4': '<A',
        '5': 'A',
        '6': '>A',
        '7': '<^A',
        '8': '^A',
        '9': '^>A'
    },
    '6': {
        'A': 'vvA',
        '0': '<vvA',
        '1': '<<vA',
        '2': '<vA',
        '3': 'vA',
        '4': '<<A',
        '5': '<A',
        '6': 'A',
        '7': '<<^A',
        '8': '<^A',
        '9': '^A'
    },
    '7': {
        'A': '>>vvvA',
        '0': '>vvvA',
        '1': 'vvA',
        '2': 'vv>A',
        '3': 'vv>>A',
        '4': 'vA',
        '5': 'v>A',
        '6': 'v>>A',
        '7': 'A',
        '8': '>A',
        '9': '>>A'
    },
    '8': {
        'A': 'vvv>A',
        '0': 'vvvA',
        '1': '<vvA',
        '2': 'vvA',
        '3': 'vv>A',
        '4': '<vA',
        '5': 'vA',
        '6': 'v>A',
        '7': '<A',
        '8': 'A',
        '9': '>A'
    },
    '9': {
        'A': 'vvvA',
        '0': '<vvvA',
        '1': '<<vvA',
        '2': '<vvA',
        '3': 'vvA',
        '4': '<<Av',
        '5': '<vA',
        '6': 'vA',
        '7': '<<A',
        '8': '<A',
        '9': 'A'
    }
}

arrows = {
    'A': {
        'A': 'A',
        '^': '<A',
        '<': 'v<<A',
        'v': '<vA',
        '>': 'vA'
    },
    '^': {
        'A': '>A',
        '^': 'A',
        '<': 'v<A',
        'v': 'vA',
        '>': 'v>A'    
    },
    '<': {
        'A': '>>^A',
        '^': '>^A',
        '<': 'A',
        'v': '>A',
        '>': '>>A'    
    },
    'v': {
        'A': '^>A',
        '^': '^A',
        '<': '<A',
        'v': 'A',
        '>': '>A'    
    },
    '>': {
        'A': '^A',
        '^': '<^A',
        '<': '<<A',
        'v': '<A',
        '>': 'A'    
    }
}                

def solve_numpad(seq):
    cur_key = 'A'
    result = []
    for c in seq:
        result.append(numpad[cur_key][c])
        cur_key = c
            
    return ''.join(result)

def solve_arrows(seq):
    result = []
    cur_char = 'A'
    for i in range(len(seq)):
        result.append(arrows[cur_char][seq[i]])
        cur_char = seq[i]
    return ''.join(result)

total = 0
for i in a:
    num = int(i[:-1])
    seq = solve_numpad(i)
    for j in range(2):
        seq = solve_arrows(seq)
    
    total += num * len(seq)

print(total)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')