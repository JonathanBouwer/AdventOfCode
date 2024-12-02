from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

GOAL_SCORE = 21
p1_wins = 0
p2_wins = 0
games = [(int(a[0][-1]), 0, 1, int(a[1][-1]), 0, 1, 1)]
score_possible = [
    (3,1),
    (4,3),
    (5,6),
    (6,7),
    (7,6),
    (8,3),
    (9,1),
]
max_len = 0
while len(games) > 0:
    p1, p1_score, p1_mult, p2, p2_score, p2_mult, turn = games.pop()
    if turn == 1:
        for move, mult in score_possible:
            new_pos = p1 + move
            new_pos = new_pos % 10
            if new_pos == 0:
                new_pos = 10
            new_score = p1_score + new_pos
            if new_score >= GOAL_SCORE:
                p1_wins += mult * p1_mult
            else:
                games.append((new_pos, new_score, mult * p1_mult, p2, p2_score, mult * p2_mult, 2))

    elif turn == 2:
        for move, mult in score_possible:
            new_pos = p2 + move
            new_pos = new_pos % 10
            if new_pos == 0:
                new_pos = 10
            new_score = p2_score + new_pos
            if new_score >= GOAL_SCORE:
                p2_wins += mult * p2_mult
            else:
                games.append((p1, p1_score, mult * p1_mult, new_pos, new_score, mult * p2_mult, 1))

print(max(p1_wins, p2_wins))

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')