from utils import load_input, parse_raw_string
a = load_input(__file__, parse_raw_string)

from time import perf_counter
t0 = perf_counter()

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

def parse_board(rows):
    board = {
        'board': [[{'val': int(row[i*3:i*3+2].strip()), 'tick': False } for i in range(BOARD_WIDTH)] for row in rows],
        'won': False
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

final_board = None
continue_index = -1
for ind, val in enumerate(nums):
    for board in boards:
        if board['won']:
            continue
        for row in board['board']:
            for j in range(BOARD_WIDTH):
                if row[j]['val'] == val:
                    row[j]['tick'] = True
                    board['sum'] -= val
                    break
            else:
                continue
            break
    
    num_board_not_won = 0
    not_won_board = None
    for board in boards:
        if board['won']:
            continue
        if board_wins(board['board']):
            board['won'] = True
        else:
            num_board_not_won += 1
            not_won_board = board
    
    if num_board_not_won == 1:
        final_board = not_won_board
        continue_index = ind + 1
        break

for new_val in nums[continue_index:]:
    for row in final_board['board']:
        for j in range(BOARD_WIDTH):
            if row[j]['val'] == new_val:
                row[j]['tick'] = True
                final_board['sum'] -= new_val
                break
        else:
            continue
        break

    if board_wins(final_board['board']):
        print(final_board['sum'] * new_val)
        break

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')