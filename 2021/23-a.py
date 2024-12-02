from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

raise Exception("Incomplete")

graph = [
    [[(1,0)]],
    [[(0,0), (2,0)]],
    [[(1,0), (2,1), (3,0)], [(2,0), (2,2)], [(2,1)]],
    [[(2,0), (4,0)]],
    [[(3,0), (4,1), (5,0)], [(4,0), (4,2)], [(4,1)]],
    [[(4,0), (6,0)]],
    [[(5,0), (6,1), (7,0)], [(6,0), (6,2)], [(6,1)]],
    [[(6,0), (8,0)]],
    [[(7,0), (8,1), (9,0)], [(8,0), (8,2)], [(8,1)]],
    [[(8,0), (10,0)]],
    [[(9,0),(11,0)]],
    [[(10,0)]]
]

vals = {
    2: {
        1: (a[2][3], 2),
        2: (a[3][1], 2)
    },
    4: {
        1: (a[2][5], 2),
        2: (a[3][3], 2)
    },
    6: {
        1: (a[2][7], 2),
        2: (a[3][5], 2)
    },
    8: {
        1: (a[2][9], 2),
        2: (a[3][7], 2)
    },
}

times = {"a": 0, "b": 0}
def time(func): 
    key = func.__name__
    def f(*args, **kwargs):
        t = perf_counter()
        result = func(*args, **kwargs) 
        if key not in times:
            times[key] = 0
        times[key] += (perf_counter() - t) * 1000
        return result
            
    return f 

costs = {"A":1,"B":10,"C":100,"D":1000}
goals = {"A":2,"B":4,"C":6,"D":8}

def get_goal(val):
    if val == "A":
        return 2
    if val == "B":
        return 4
    if val == "C":
        return 6
    if val == "D":
        return 8

@time
def is_done(pieces):
    for x, col in pieces.items():
        for y, (val, rem_moves) in col.items():
            if not x == get_goal(val):
                return False
    return True
    
@time
def min_remaining_cost(pieces):
    cost = 0
    for x, col in pieces.items():
        for y, (val, rem_moves) in col.items():
            g = get_goal(val)
            if x == g:
                continue
            cost += costs[val] * (1 + y + abs(x - g))
    return cost

BEST_COST_SO_FAR = 999999999
def make_moves(pieces, cost, depth=0):
    global BEST_COST_SO_FAR
    
    valid_moves = []
    t1 = perf_counter()
    for x, col in pieces.items():
        for y, (val, rem_moves) in col.items():
            if rem_moves == 0:
                continue
            g = get_goal(val)
            if x == g:
                if y == 2:
                    continue
                if pieces[x][2] and x == get_goal(pieces[x][2][0]):
                    continue

            move_queue = []
            for n in graph[x][y]:
                if not n[0] in pieces or n[1] not in pieces[n[0]]:
                    move_queue.append((n, costs[val]))

            seen = [[False for v in range(3)] for c in range(12)]
            vm = []
            for move, sub_cost in move_queue:
                mx, my = move
                seen[mx][my] = True
                should_append = True
                if mx in [2,4,6,8] and my == 0:
                    should_append = False
                elif my != 0:
                    if y != 0 or mx != g:
                        should_append = False
                elif rem_moves == 1 and mx != g:
                    should_append = False
                if should_append:
                    vm.append((cost + sub_cost, (x, y), val, rem_moves, move))
                for nx, ny in graph[mx][my]:
                    if not seen[nx][ny] and not pieces.get(nx,{}).get(ny, None):
                        move_queue.append(((nx, ny), sub_cost + costs[val]))
            goal_moves = []
            for (sub_cost, pos, val, rem_moves, move) in vm:
                if move[0] == g and move[1] != 0:
                    goal_moves.append((sub_cost, pos, val, rem_moves, move))
                
            if len(goal_moves) > 0:
                valid_moves.extend(goal_moves)
            else:
                valid_moves.extend(vm)
    times["a"] += (perf_counter() - t1) * 1000
    
    best_move = None
    best_cost = 999999999999
    valid_moves.sort()
    for i, (sub_cost, pos, val, rem_moves, move) in enumerate(valid_moves):
        t2 = perf_counter()
        if depth < 2:
            print(depth, f"{i}/{len(valid_moves)}", pos, val, rem_moves, move)
        if sub_cost > BEST_COST_SO_FAR:
            times["b"] += (perf_counter() - t2) * 1000
            continue
        new_pieces = {px: {py: pv for py, pv in col.items()} for px, col in pieces.items()}
        del new_pieces[pos[0]][pos[1]]
        if move[0] not in new_pieces:
            new_pieces[move[0]] = {}
        new_pieces[move[0]][move[1]] = (val, rem_moves - 1)
        if sub_cost + min_remaining_cost(new_pieces) > BEST_COST_SO_FAR:
            times["b"] += (perf_counter() - t2) * 1000
            continue
        times["b"] += (perf_counter() - t2) * 1000
        if is_done(new_pieces):
            move_string, move_cost = "You're done", sub_cost
        else:
            move_string, move_cost = make_moves(new_pieces, sub_cost, depth+1)
        t3 = perf_counter()
        if move_cost < best_cost:
            best_move = f"Move {val} from {pos} to {move} for {sub_cost}\n" + move_string
            best_cost = move_cost
            if best_cost < BEST_COST_SO_FAR:
                print(best_cost)
                BEST_COST_SO_FAR = best_cost
        times["b"] += (perf_counter() - t3) * 1000

    return best_move, best_cost
        
best_move, best_cost = make_moves(vals, 0)
print(best_move)
print(best_cost)
print(times)
    
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')