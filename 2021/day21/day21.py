from collections import defaultdict
from typing import Tuple

test_data = ["Player 1 starting position: 4", "Player 2 starting position: 8"]
lines = [
    "Player 1 starting position: 2",
    "Player 2 starting position: 1",
]

# data = test_data
data = lines


def practice_game():
    s = dict()
    for d in data:
        key, pos = d.split(" starting position: ")
        key = "p1" if key == "Player 1" else "p2"
        s[key] = {
            "pos": int(pos),
            "score": 0,
        }

    hi_score = 0
    die_val = 0
    rolls = 0
    turns = 0
    while hi_score < 1000:
        p = "p1" if turns % 2 == 0 else "p2"
        turns += 1

        # roll 3 times
        die_score = 0
        for i in range(die_val + 1, die_val + 4):
            die_val += 1
            if die_val > 100:
                die_val -= 100
            rolls += 1
            die_score += i

        # find the new space
        space = (s[p]["pos"] + die_score) % 10
        space = 10 if space == 0 else space
        s[p]["pos"] = space
        s[p]["score"] += space

        hi_score = max([s["p1"]["score"], s["p2"]["score"]])
        lo_score = min([s["p1"]["score"], s["p2"]["score"]])
    return rolls * lo_score


ans1 = practice_game()
print(ans1)


def play_real_game(pos1: int, pos2: int) -> Tuple[int, int]:
    outcomes = defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                outcomes[i + j + k] += 1

    positions = {i: defaultdict(int) for i in range(1, 11)}
    for pos in positions.keys():
        for score in outcomes:
            positions[pos][(pos - 1 + score) % 10 + 1] += outcomes[score]

    p1_wins, p2_wins = 0, 0
    p1_scores = defaultdict(lambda: defaultdict(int), {0: {pos1: 1}})
    p2_scores = defaultdict(lambda: defaultdict(int), {0: {pos2: 1}})

    while p1_scores and p2_scores:
        next_scores = defaultdict(lambda: defaultdict(int))

        for score, pos_list in p1_scores.items():
            for pos, universes in pos_list.items():
                for next_pos, universe_count in positions[pos].items():
                    next_score = score + next_pos
                    next_outcomes = universes * universe_count

                    if next_score >= 21:

                        # sum all the universes where the other player loses
                        p1_wins += next_outcomes * sum(
                            x for pl in p2_scores.values() for x in pl.values()
                        )

                    else:

                        # otherwise, record the number of universes active at the next played position
                        next_scores[next_score][next_pos] += next_outcomes

        p1_scores = next_scores

        # swap the players and play again
        p1_scores, p2_scores = p2_scores, p1_scores
        p1_wins, p2_wins = p2_wins, p1_wins

    return p1_wins, p2_wins


ans2 = play_real_game(2, 1)
print(ans2)
