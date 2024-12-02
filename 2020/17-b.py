from time import perf_counter
t0 = perf_counter()

a = [
"####.#..",
".......#",
"#..#####",
".....##.",
"##...###",
"#..#.#.#",
".##...#.",
"#...##.."
]

a_small = [
".#.",
"..#",
"###"
]

board = {}


def set_board(board_to_set, x, y, z, w, val):
    if w not in board_to_set:
        board_to_set[w] = {}
    if z not in board_to_set[w]:
        board_to_set[w][z] = {}
    if y not in board_to_set[w][z]:
        board_to_set[w][z][y] = {}
    board_to_set[w][z][y][x] = val


def set_board_active(board_to_set, x, y, z, w):
    set_board(board_to_set, x, y, z, w, 1)


def set_board_inactive(board_to_set, x, y, z, w):
    set_board(board_to_set, x, y, z, w, 0)

    
def get_board(x, y, z, w):
    if w not in board:
        return 0
    if z not in board[w]:
        return 0
    if y not in board[w][z]:
        return 0
    if x not in board[w][z][y]:
        return 0
    return board[w][z][y][x]


def get_board_range():
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    min_w = min(board.keys())
    max_w = max(board.keys())
    for kw, vw in board.items():
        min_z = min(min_z, min(vw.keys()))
        max_z = max(max_z, max(vw.keys()))
        for kz, vz in vw.items():
            min_y = min(min_y, min(vz.keys()))
            max_y = max(max_y, max(vz.keys()))
            for ky, vy in vz.items():
                min_x = min(min_x, min(vy.keys()))
                max_x = max(max_x, max(vy.keys()))
            
    return (min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w)


def simulate_board():
    global board
    (min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w) = get_board_range()
    new_board = {}
    for w in range(min_w - 1, max_w + 2):
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    surroud_sum = 0
                    for winc in range(-1, 2):
                        for zinc in range(-1, 2):
                            for yinc in range(-1, 2):
                                for xinc in range(-1, 2):
                                    surroud_sum += get_board(x + xinc, y + yinc, z + zinc, w + winc)
                    surroud_sum -= get_board(x, y, z, w)
                    
                    if get_board(x, y, z, w) == 1:
                        if surroud_sum == 2 or surroud_sum == 3:
                            set_board_active(new_board, x, y, z, w)
                    else:
                        if surroud_sum == 3:
                            set_board_active(new_board, x, y, z, w)
    
    board = new_board


def count_board():
    total = 0
    (min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w) = get_board_range()
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    total += get_board(x, y, z, w)
                
    return total

def main():
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "#":
                set_board_active(board, j, i, 0, 0)

    for i in range(6):
        simulate_board()
        
    print(count_board())


main()
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')