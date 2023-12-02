import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def rock_list(rocks):
    rl = []
    r = []
    i = 0
    for idx, line in enumerate(rocks):
        if line == "":
            rl.append(r)
            r = []
            i = 0
        else:
            tmp = []
            for j, char in enumerate(line):
                tmp.append(char)
            r.append(tmp)
            i += 1

        if idx == len(rocks) - 1:
            rl.append(r)
    return rl


def tetris(num_rocks, rocks, wind_list):
    w = 7  # cave width
    board = []
    init_board = [".", ".", ".", ".", ".", ".", "."]
    wind_idx = 0
    rock_idx = 0
    cache = {}
    for i in range(num_rocks):
        rock = rocks[rock_idx]
        rock_idx += 1
        if rock_idx > len(rocks) - 1:
            rock_idx = 0
        # extend the width of the rock
        new_rock = []
        for line in rock:
            new_line = [".", "."] + line + ["." for i in range(w - len(line) - 2)]
            new_rock.append(new_line)

        prev_board = board
        board = (
            [line for line in new_rock]
            + [
                init_board.copy(),
                init_board.copy(),
                init_board.copy(),
            ]
            + [line for line in prev_board]
        )

        rock_idxs = []
        for i, line in enumerate(new_rock):
            for j, char in enumerate(new_rock[i]):
                if new_rock[i][j] == "#":
                    rock_idxs.append((i, j))

        while True:
            # wind blows
            wind = wind_list[wind_idx]  # get the current wind

            rock_idxs, board = shift(rock_idxs, board, wind)
            wind_idx += 1
            # reset back to start
            if wind_idx > len(wind_list) - 1:
                wind_idx = 0

            # rock falls
            prev_rock_idxs = rock_idxs
            rock_idxs, board = fall(rock_idxs, board)

            if rock_idxs == prev_rock_idxs:
                break
        # trim any blank lines from the board
        for i in range(board.count(init_board.copy())):
            board.remove(init_board.copy())

        # print("")
        # print("\n".join([" ".join([str(cell) for cell in row]) for row in board]))

    return len(board)


def shift(rock_idxs, board, wind):
    new_x = -1 if wind == "<" else 1
    shifted_idxs = [(c[0], c[1] + new_x) for c in rock_idxs]
    sxs = [c[1] for c in shifted_idxs]
    max_x = max(sxs)
    min_x = min(sxs)
    boundary_idxs = []
    for y, x in rock_idxs:
        if (y, x + new_x) not in rock_idxs:
            boundary_idxs.append((y, x + new_x))

    # no shift
    if max_x > 6 or min_x < 0:
        return rock_idxs, board

    for y, x in boundary_idxs:
        if board[y][x] == "#":
            return rock_idxs, board

    # if we havent returned yet...
    for y, x in rock_idxs:
        board[y][x] = "."

    for y, x in shifted_idxs:
        board[y][x] = "#"

    return shifted_idxs, board


def fall(rock_idxs, board):
    shifted_idxs = [(c[0] + 1, c[1]) for c in rock_idxs]
    boundary_idxs = []
    for y, x in rock_idxs:
        if (y + 1, x) not in rock_idxs:
            boundary_idxs.append((y + 1, x))

    for y, x in boundary_idxs:
        try:
            if board[y][x] == "#":
                return rock_idxs, board
        except:
            return rock_idxs, board

    for y, x in rock_idxs:
        board[y][x] = "."

    for y, x in shifted_idxs:
        board[y][x] = "#"

    return shifted_idxs, board


def solve(input, rocks):
    rl = rock_list(rocks)
    ans1 = tetris(2022, rl, input)
    # ans2 = tetris(1000000000000, rl, input)
    return ans1


rocks = [
    "####",
    "",
    ".#.",
    "###",
    ".#.",
    "",
    "..#",
    "..#",
    "###",
    "",
    "#",
    "#",
    "#",
    "#",
    "",
    "##",
    "##",
]
test_data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
data = get_data(day=17, year=2022)
print(solve(test_data, rocks))


ans1 = solve(data, rocks)
# submit(ans1, day=17, year=2022, part="a")

# no idea how to do part 2
