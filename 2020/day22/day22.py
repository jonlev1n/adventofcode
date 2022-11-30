import copy
import time
import re
import math
import numpy as np
import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)


# file = open("/Users/jon/git/adventofcode2020/day22/test_input.txt", "r")
# file = open("/Users/jon/git/adventofcode2020/day22/test_input2.txt", "r")
file = open("/Users/jon/git/adventofcode2020/day22/input.txt", "r")


lines = file.read().splitlines()
p1 = []
p2 = []


def read():
    p1_deck = False
    p2_deck = False
    for line in lines:
        if line == "\n" or line == "":
            pass
        else:
            if "Player 1" in line:
                p1_deck = True
                p2_deck = False
            elif "Player 2" in line:
                p1_deck = False
                p2_deck = True
            else:
                if p1_deck:
                    p1.append(int(line))
                elif p2_deck:
                    p2.append(int(line))


def get_winner(p1, p2):
    # print("getting winner")
    # print(p1, p2)
    w = max(len(p1), len(p2))
    if len(p1) == w:
        return [p1, True]
    else:
        return [p2, False]


def part1(p1, p2):

    # print(top_card)
    # print(p1)
    while len(p1) > 0 and len(p2) > 0:
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)

        w = max(p1_card, p2_card)
        l = min(p1_card, p2_card)

        if w == p1_card:
            # give both cards to p1
            p1 = p1 + [w, l]
        else:
            # give both to p2
            p2 = p2 + [w, l]

    winner = get_winner(p1, p2)[0]
    score = sum(card * (len(winner) - idx) for idx, card in enumerate(winner))
    print("Part 1: %d" % score)


read()

# part1(p1, p2)

previous_decks = {"0": []}


def part2(p1, p2, game):
    # print("======== game: %d =======" % game)
    # print("p1's deck: %s" % p1)
    # print("p2's deck: %s" % p2)

    if game > 0 and any([p1, p2] == item for item in previous_decks[str(game)]):
        # print("breaking!")
        return [p1, True]
    else:
        if len(p1) == 0 or len(p2) == 0:
            # return the winning array
            return get_winner(p1, p2)

        previous_decks[str(game)].append([copy.deepcopy(p1), copy.deepcopy(p2)])
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        # print("p1 plays: %d" % p1_card)
        # print("p2 plays: %d" % p2_card)

        if len(p1) >= p1_card and len(p2) >= p2_card:
            # recurse
            # print("Dropping into sub-game!")
            new_p1 = copy.deepcopy(p1[0:p1_card])
            new_p2 = copy.deepcopy(p2[0:p2_card])
            # games_played = [key for key in previous_decks.keys()]
            new_game = int(list(previous_decks.keys())[-1]) + 1
            # while str(new_game) in games_played:
            #     new_game += 1
            # print("games played: %s" % games_played)
            # print("next game: %d" % new_game)
            previous_decks[str(new_game)] = []
            w = part2(new_p1, new_p2, new_game)
            # print("w: ")
            # print(w)
            deck = w[0]
            w_c = p1_card if w[1] else p2_card
            l_c = p2_card if w[1] else p1_card
            w_d = p1 if w[1] else p2
            l_d = p2 if w[1] else p1
            # print(deck)
            # print(p1)
            # print(p2)
            if p1 == w_d:
                p1 = p1 + [w_c, l_c]
            else:
                p2 = p2 + [w_c, l_c]
            # print(w_d, l_d)
            # print(w_c, l_c)
            # print(p1_card, p2_card)
            # print(p1, p2)
            return part2(p1, p2, game)
        else:
            w = max(p1_card, p2_card)
            l = min(p1_card, p2_card)
            if w == p1_card:
                # give both cards to p1
                p1 = p1 + [w, l]
            else:
                # give both to p2
                p2 = p2 + [w, l]
            # recurse
            return part2(p1, p2, game)
            # print("next: %s" % nxt)


start_time = time.time()
w = part2(p1, p2, 0)
print(time.time() - start_time)
pt2 = sum(card * (len(w[0]) - idx) for idx, card in enumerate(w[0]))
print("Part 2: %d" % pt2)
