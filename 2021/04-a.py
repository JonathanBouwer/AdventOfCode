from utils import load_input, parse_raw_string
a = load_input(__file__, parse_raw_string)

from time import perf_counter
t0 = perf_counter()

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

def parse_board(rows):
    board = {
        'board': [[{'val': int(row[i*3:i*3+2].strip()), 'tick': False } for i in range(BOARD_WIDTH)] for row in rows]
    }
    board['sum'] = sum(sum(val['val'] for val in row) for row in board['board'])
    return board

def board_wins(board):
    # ROWS
    for row in board:
        for val in row:
            if not val['tick']:
                break
        else:
            return True
        
    # COLUMNS
    for j in range(BOARD_WIDTH):
        for row in board:
            if not row[j]['tick']:
                break
        else:
            return True
            
    return False

nums = [int(x) for x in a[0].split(',')]

boards = []
current_board = []
for row in a[2:]:
    if len(row) == 0:
        boards.append(parse_board(current_board))
        current_board = []
        continue
    current_board.append(row)

for val in nums:
    for board in boards:
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if board['board'][i][j]['val'] == val:
                    board['board'][i][j]['tick'] = True
                    board['sum'] -= val
                    break
            else:
                continue
            break
    
    for board in boards:
        if board_wins(board['board']):
            print(board['sum'] * val)
            break
    else:
        continue
    break

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')