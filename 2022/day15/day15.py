import os
from aocd import lines, submit, get_data
import re, math, numpy as np

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


scan_row = 2000000
non_beacons = set()

discs = []
for line in lines:
    sx, sy, bx, by = (int(z[1:]) for z in re.findall(r"=-?\d+", line))
    radius = abs(bx - sx) + abs(by - sy)
    discs.append((sx, sy, radius))

    dist_to_scan_row = abs(scan_row - sy)
    num_steps_left = radius - dist_to_scan_row

    if num_steps_left < 0:
        continue

    for x in range(sx - num_steps_left, sx + num_steps_left + 1):
        pos = (x, scan_row)
        if pos != (bx, by):
            non_beacons.add(pos)
ans1 = len(non_beacons)


def get_boundary(x, y, r):
    temp = (x, y + r)
    while temp != (x + r, y):
        temp = (temp[0] + 1, temp[1] - 1)
        yield temp
    while temp != (x, y - r):
        temp = (temp[0] - 1, temp[1] - 1)
        yield temp
    while temp != (x - r, y):
        temp = (temp[0] - 1, temp[1] + 1)
        yield temp
    while temp != (x, y + r):
        temp = (temp[0] + 1, temp[1] + 1)
        yield temp


# part 2
for x, y, r in discs:
    print("disc {} {} {}".format(x, y, r))
    for px, py in get_boundary(x, y, r + 1):
        if 0 <= px <= 4000000 and 0 <= py <= 4000000:
            for dx, dy, dr in discs:
                if (abs(px - dx) + abs(py - dy)) <= dr:

                    break
            else:
                print("beacon:", px, py)
                ans2 = 4000000 * px + py
                break


submit(ans1, day=15, year=2022, part="a")
submit(ans2, day=15, year=2022, part="b")
