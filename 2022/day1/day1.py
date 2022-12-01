import os

from aocd import lines, submit

# test_data = []
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# def read_data():
#     with open(os.path.join(__location__, "input.txt")) as input:
#         data = input.read()
#     return data


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
l = len(ans)
pt1 = ans[l - 1]
submit(pt1, part="a", day=1, year=2022)

pt2 = ans[l - 1] + ans[l - 2] + ans[l - 3]
submit(pt2, part="b", day=1, year=2022)
