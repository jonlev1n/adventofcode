import os

from aocd import lines, submit

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input):
    sums = []
    cur_sum = 0
    for line in input:
        try:
            cur_sum += int(line)
        except:
            sums.append(cur_sum)
            cur_sum = 0

    return sorted(sums)


ans = solve(lines)
pt1 = ans[len(ans) - 1]
submit(pt1, part="a", day=1, year=2022)

pt2 = ans[len(ans) - 1] + ans[len(ans) - 2] + ans[len(ans) - 3]
print(pt2)
submit(pt2, part="b", day=1, year=2022)
