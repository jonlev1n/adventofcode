import os
from aocd import lines, submit, get_data

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def get_start_finish(input):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == "S":
                start = (i, j)
            if input[i][j] == "E":
                end = (i, j)
    return (start, end)


def solve(input):
    (start, end) = get_start_finish(input)
    print(start, end)


test_data = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]
test_ans = solve(test_data)
print(test_ans)


ans1 = solve(lines)
# submit(ans1, day=12, year=2022, part="a")
ans2 = solve(lines)
# submit(ans2, day=12, year=2022, part="b")
