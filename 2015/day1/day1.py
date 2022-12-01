import os
from aocd import lines, submit, get_data

# test_data = []
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# def read_data():
# 	with open(os.path.join(__location__, 'input.txt')) as input:
# 		data = input.read()
# 	return data


def solve(input):
    count = 0
    index = 0
    for idx, char in enumerate(input):
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count == -1 and index == 0:
            index = idx + 1

    return count, index


data = get_data(day=1, year=2015)
(ans1, ans2) = solve(data)
submit(ans1, day=1, part="a", year=2015)
submit(ans2, day=1, part="b", year=2015)
