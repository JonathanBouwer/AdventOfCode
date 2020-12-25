from time import time
t0 = time()

p1 = [
26,
14,
6,
34,
37,
9,
17,
39,
4,
5,
1,
8,
49,
16,
18,
47,
20,
31,
23,
19,
35,
41,
28,
15,
44
]

p2 = [
7,
2,
10,
25,
29,
46,
40,
45,
11,
50,
42,
24,
38,
13,
36,
22,
33,
3,
43,
21,
48,
30,
32,
12,
27
]

def play_recursive_combat(p1_deck, p2_deck):
    seen = set()
    while True:
        decks = f"{p1_deck}-{p2_deck}"
        if decks in seen or len(p2_deck) == 0:
            final_winner = 1
            break
        elif len(p1_deck) == 0:
            final_winner = 2
            break

        seen.add(decks)

        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            winner = play_recursive_combat(p1_deck[:p1_card], p2_deck[:p2_card])[0]
        else:
            winner = 1 if p1_card > p2_card else 2
            
        if winner == 1:
            p1_deck.extend((p1_card, p2_card))
        else:
            p2_deck.extend((p2_card, p1_card))
            
    winning_deck = p1_deck if final_winner == 1 else p2_deck
    score = 0
    for i in range(len(winning_deck)):
        score += winning_deck[i] * (len(winning_deck) - i)

    return (final_winner, score)

# p1 = [9,2,6,3,1]
# p2 = [5,8,4,7,10]
# p1 = [43,19]
# p2 = [2,29,14]

final_winner, score = play_recursive_combat(p1, p2)
print(score)

print(f'Time: {(time()-t0) * 1000}ms')