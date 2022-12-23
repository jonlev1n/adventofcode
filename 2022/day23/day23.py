import os
from aocd import lines, submit, get_data
import numpy as np


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


POSITIONS = {
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, 1),
    "W": (0, -1),
    "E": (0, 1),
    "SW": (1, -1),
    "S": (1, 0),
    "SE": (1, 1),
}

ORDER = ["N", "S", "W", "E"]

# maps what you need to check to the direction
CHECK = {
    "N": ["NW", "N", "NE"],
    "E": ["NE", "E", "SE"],
    "S": ["SE", "S", "SW"],
    "W": ["SW", "W", "NW"],
}


def solve(input):
    field = np.zeros((len(input), len(input[0])), dtype=str)
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            field[i][j] = char
    f1 = field.copy()
    f2 = field.copy()

    f1, _ = moveElves(f1, 10)
    ly, _ = np.where(f1 == ".")
    ans1 = len(ly)
    print("ans1 is:", ans1)
    print("")
    # reset the order
    global ORDER
    ORDER = ["N", "S", "W", "E"]
    f2, ans2 = moveElves(f2, 1000000)
    print("ans2 is:", ans2)

    return ans1, ans2


def moveElves(field, iter):
    for z in range(iter):
        # first pad the field if there are any elves along the edges
        min_x = 0
        min_y = 0
        max_x = len(field[0]) - 1
        max_y = len(field) - 1
        perim = (
            list(field[min_y, :])
            + list(field[max_y, :])
            + list(field[:, min_x])
            + list(field[:, max_x])
        )

        if any([p == "#" for p in perim]):
            field = padF(field)

        # get all the elf indices
        e_y, e_x = np.where(field == "#")
        elves = [(e_y[i], e_x[i]) for i in range(len(e_y))]

        proposed = {}
        for e in elves:
            proposed[e] = None
            # check all 8 spaces around - if nothing is there, skip
            if not any(
                field[tuple(np.add(e, p))[0]][tuple(np.add(e, p))[1]] == "#"
                for p in POSITIONS.values()
            ):
                # dont_move.append(e)
                continue

            for d in ORDER:
                # get the 3 spaces to check
                checks = CHECK[d]
                spaces = []
                for c in checks:
                    spaces.append(tuple(np.add(e, POSITIONS[c])))
                # then check the spaces
                if not any([field[s[0]][s[1]] == "#" for s in spaces]):
                    proposed[e] = tuple(np.add(e, POSITIONS[d]))
                    break

        # if two elves propose going to the same spot, they dont move
        values = proposed.values()
        keys = proposed.keys()
        dont_move = []
        for v in values:
            m = []
            for k in keys:
                if proposed[k] == v:
                    m.append(k)
            if len(m) > 1:  # 2 or more keys match a given value
                dont_move += m
        dont_move = list(set(dont_move))
        # if every elf doesnt move, return
        if all([p == None for p in proposed.values()]):
            return cropF(field), z + 1
        # now move the elves
        for e in keys:
            if e not in dont_move and proposed[e] is not None:
                field[e[0]][e[1]] = "."
                ny, nx = proposed[e]
                field[ny][nx] = "#"

        # mutate the order of direction checks
        last = ORDER.pop(0)
        ORDER.append(last)
    field = cropF(field)
    return field, z


def padF(field):
    return np.pad(field, pad_width=1, mode="constant", constant_values=".")


def cropF(field):
    y, x = np.where(field == "#")
    min_y = min(y)
    max_y = max(y)
    min_x = min(x)
    max_x = max(x)

    field = field[min_y : max_y + 1, min_x : max_x + 1]
    return field


test_data = [
    "....#..",
    "..###.#",
    "#...#.#",
    ".#...##",
    "#.###..",
    "##.#.##",
    ".#..#..",
]

# test_data = [
#     ".....",
#     "..##.",
#     "..#..",
#     ".....",
#     "..##.",
#     ".....",
# ]

# solve(test_data)
ans1, ans2 = solve(lines)
submit(ans1, day=23, year=2022, part="a")
submit(ans2, day=23, year=2022, part="b")
