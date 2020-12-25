from time import time
t0 = time()

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
a = [
".#.",
"..#",
"###"
]
board = {}


def set_board(board_to_set, x, y, z, val):
    if z not in board_to_set:
        board_to_set[z] = {}
    if y not in board_to_set[z]:
        board_to_set[z][y] = {}
    board_to_set[z][y][x] = val


def set_board_active(board_to_set, x, y, z):
    set_board(board_to_set, x, y, z, 1)


def set_board_inactive(board_to_set, x, y, z):
    set_board(board_to_set, x, y, z, 0)

    
def get_board(x, y, z):
    if z not in board:
        return 0
    if y not in board[z]:
        return 0
    if x not in board[z][y]:
        return 0
    return board[z][y][x]


def get_board_range():
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = min(board.keys())
    max_z = max(board.keys())
    for kz, vz in board.items():
        min_y = min(min_y, min(vz.keys()))
        max_y = max(max_y, max(vz.keys()))
        for ky, vy in vz.items():
            min_x = min(min_x, min(vy.keys()))
            max_x = max(max_x, max(vy.keys()))
            
    return (min_x, max_x, min_y, max_y, min_z, max_z)


def simulate_board():
    global board
    (min_x, max_x, min_y, max_y, min_z, max_z) = get_board_range()
    new_board = {}
    for z in range(min_z - 1, max_z + 2):
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                surroud_sum = 0
                surroud_sum += get_board(x + 1, y + 1, z + 1)
                surroud_sum += get_board(x + 1, y + 1, z)
                surroud_sum += get_board(x + 1, y + 1, z - 1)
                surroud_sum += get_board(x + 1, y, z + 1)
                surroud_sum += get_board(x + 1, y, z)
                surroud_sum += get_board(x + 1, y, z - 1)
                surroud_sum += get_board(x + 1, y - 1, z + 1)
                surroud_sum += get_board(x + 1, y - 1, z)
                surroud_sum += get_board(x + 1, y - 1, z - 1)
                
                surroud_sum += get_board(x, y + 1, z + 1)
                surroud_sum += get_board(x, y + 1, z)
                surroud_sum += get_board(x, y + 1, z - 1)
                surroud_sum += get_board(x, y, z + 1)
                # surroud_sum += get_board(x, y, z)
                surroud_sum += get_board(x, y, z - 1)
                surroud_sum += get_board(x, y - 1, z + 1)
                surroud_sum += get_board(x, y - 1, z)
                surroud_sum += get_board(x, y - 1, z - 1)
                
                surroud_sum += get_board(x - 1, y + 1, z + 1)
                surroud_sum += get_board(x - 1, y + 1, z)
                surroud_sum += get_board(x - 1, y + 1, z - 1)
                surroud_sum += get_board(x - 1, y, z + 1)
                surroud_sum += get_board(x - 1, y, z)
                surroud_sum += get_board(x - 1, y, z - 1)
                surroud_sum += get_board(x - 1, y - 1, z + 1)
                surroud_sum += get_board(x - 1, y - 1, z)
                surroud_sum += get_board(x - 1, y - 1, z - 1)
                
                if get_board(x, y, z) == 1:
                    if surroud_sum == 2 or surroud_sum == 3:
                        set_board_active(new_board, x, y, z)
                else:
                    if surroud_sum == 3:
                        set_board_active(new_board, x, y, z)
    
    board = new_board


def print_board():
    (min_x, max_x, min_y, max_y, min_z, max_z) = get_board_range()
    for z in range(min_z, max_z + 1):
        print(f"{z=}")
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                print("#" if get_board(x, y, z) == 1 else ".", end="")
            print()
        print()


def count_board():
    total = 0
    (min_x, max_x, min_y, max_y, min_z, max_z) = get_board_range()
    for z in range(min_z, max_z + 1):
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                total += get_board(x, y, z)
                
    return total

def main():
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "#":
                set_board_active(board, j, i, 0)

    # print_board()
    for i in range(6):
        # print(f"After {i + 1} cycle{'s' if i > 0 else ''}:")
        simulate_board()
        # print_board()
        
    print(count_board())


main()
print(f'Time: {(time()-t0) * 1000}ms')