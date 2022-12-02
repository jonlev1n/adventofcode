import os
from aocd import lines, submit

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    points = {"X": 1, "Y": 2, "Z": 3}
    wins = ["A Y", "C X", "B Z"]
    draws = ["A X", "B Y", "C Z"]
    win = 6
    draw = 3

    score = 0
    for l in input:
        if l in wins:
            score += win
        if l in draws:
            score += draw

        score += points[l[2]]

    return score


def solve_b(input):
    points = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
    combos = {
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
        "Z": {"A": "B", "B": "C", "C": "A"},
    }

    score = 0
    for l in input:
        play = combos[l[2]][l[0]]
        score += points[play] + points[l[2]]

    return score


ans1 = solve_a(lines)
submit(ans1, day=2, year=2022, part="a")
ans2 = solve_b(lines)
submit(ans2, day=2, year=2022, part="b")
