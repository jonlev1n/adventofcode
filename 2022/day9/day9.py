import os
from aocd import lines, submit, get_data
import numpy as np


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input, len_rope):
    # start position is 0,0 for H and T
    rope = [(0, 0) for i in range(0, len_rope)]
    tails = [(0, 0)]
    count = 0
    for line in input:
        [direc, num_moves] = line.split()
        if direc == "R":
            h_move = (1, 0)
        if direc == "L":
            h_move = (-1, 0)
        if direc == "U":
            h_move = (0, 1)
        if direc == "D":
            h_move = (0, -1)

        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for k in range(0, int(num_moves)):
            count += 1
            for i in range(0, len_rope - 1):
                h = rope[i]
                t = rope[i + 1]

                if i == 0:
                    hm = h_move
                    h = tuple(np.add(h, hm))

                diff = tuple(np.subtract(h, t))
                tm = (0, 0)  # init as no move
                s = [tuple(np.add(t, n)) for n in neighbors]
                if h not in s:
                    if any(ele == 0 for ele in diff):
                        if diff[0] == 0:
                            if diff[1] < 0:
                                tm = (0, -1)
                            else:
                                tm = (0, 1)
                        else:
                            if diff[0] < 0:
                                tm = (-1, 0)
                            else:
                                tm = (1, 0)
                    elif all(ele > 0 for ele in diff):
                        tm = (1, 1)  # top right
                    elif all(ele < 0 for ele in diff):
                        tm = (-1, -1)  # bottom left
                    else:
                        if diff[0] < 1:
                            tm = (-1, 1)  # top left
                        else:
                            tm = (1, -1)  # bottom right

                    t = tuple(np.add(t, tm))
                rope[i] = h
                rope[i + 1] = t

            if rope[len(rope) - 1] not in tails:
                tails.append(t)

        num_spaces = len(tails)

    return num_spaces


test_data = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]

test_data_b = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20",
]

# test_ans = solve(test_data, 2)
test_ans_b = solve(test_data_b, 10)


ans1 = solve(lines, 2)
submit(ans1, day=9, year=2022, part="a")
ans1 = solve(lines, 10)
submit(ans1, day=9, year=2022, part="b")
