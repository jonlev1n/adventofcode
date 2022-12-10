import os
from aocd import lines, submit, get_data
from test_data import test_data

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input):
    register = {0: 0}
    hot_cycles = [20, 60, 100, 140, 180, 220]
    vals = []
    for line in input:
        if "addx" in line:
            register[max(register.keys()) + 2] = int(line.split()[1])
        if "noop" in line:
            register[max(register.keys()) + 1] = 0

    X = 1
    crt = ""
    crt_position = 0
    crt_max = 39
    for i in range(1, max(register.keys()) + 1):
        if crt_position > crt_max:
            crt_position = 0

        sprite = [X - 1, X, X + 1]
        if crt_position in sprite:
            crt += "#"
        else:
            crt += "."

        if i in hot_cycles:
            vals.append((i) * X)

        if i in register.keys():
            X += register[i]

        crt_position += 1
        # print(X)
    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:240])
    return sum(vals)


# test_ans = solve(test_data)
# print(test_ans)


ans1 = solve(lines)
submit(ans1, day=10, year=2022, part="a")

####.###...##..###..####.###...##....##.
#....#..#.#..#.#..#.#....#..#.#..#....#.
###..#..#.#....#..#.###..#..#.#.......#.
#....###..#....###..#....###..#.......#.
#....#.#..#..#.#.#..#....#....#..#.#..#.
####.#..#..##..#..#.####.#.....##...##..

# output ^^
ans2 = "ERCREPCJ"
submit(ans2, day=10, year=2022, part="b")
