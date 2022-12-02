import os
from aocd import lines, submit, get_data
from hashlib import md5


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input, leader):
    x = 0
    while True:
        x += 1
        line = "%s%d" % (input, x)

        h = md5(line.encode())
        digest = h.hexdigest()
        # if digest[0:5] == "00000":
        if digest[0 : len(leader)] == leader:
            break
    return x


ans1 = solve("ckczppom", "00000")
ans2 = solve("ckczppom", "000000")
submit(ans1, day=4, year=2015, part="a")
submit(ans2, day=4, year=2015, part="b")
