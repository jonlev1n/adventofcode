from aocd import lines, submit, get_data
import re
from PIL import Image
import numpy as np


test_data = [
    "p=0,4 v=3,-3",
    "p=6,3 v=-1,-3",
    "p=10,3 v=-1,2",
    "p=2,0 v=2,-1",
    "p=0,0 v=1,3",
    "p=3,0 v=-2,-2",
    "p=7,6 v=-1,-3",
    "p=3,0 v=-1,-2",
    "p=9,3 v=2,3",
    "p=7,3 v=-1,2",
    "p=2,4 v=2,-3",
    "p=9,5 v=-3,-3",
]


def part1():
    # data = test_data
    data = lines
    h = 103
    w = 101
    minX = 0
    minY = 0
    xR = range(minX, w)
    yR = range(minY, h)
    ticks = 100

    robots = []
    for row in data:
        x, y, vx, vy = map(int, re.findall(r"\-?\d+", row))
        robots.append(list((x, y, vx, vy)))

    p = []
    for r in robots:
        for _ in range(0, ticks):
            r[0] += r[2]
            r[1] += r[3]
            if r[0] not in xR:
                if r[2] > 0:
                    r[0] -= w
                else:
                    r[0] += w
            if r[1] not in yR:
                if r[3] > 0:
                    r[1] -= h
                else:
                    r[1] += h

        p.append((r[0], r[1]))

    q1, q2, q3, q4 = 0, 0, 0, 0
    midX = int((w - 1) / 2)
    midY = int((h - 1) / 2)
    for r in p:
        x, y = r
        if x == midX or y == midY:
            pass

        elif x in range(0, midX):
            if y in range(0, midY):
                q1 += 1
            else:
                q2 += 1
        else:
            if y in range(0, midY):
                q3 += 1
            else:
                q4 += 1

    ans1 = q1 * q2 * q3 * q4
    print(ans1)
    return ans1


def print_map(m, w, h):
    image = Image.new("1", (w, h))

    for x in range(w):
        for y in range(h):
            if m[y][x] == 0:
                image.putpixel((x, y), 0)
            else:
                image.putpixel((x, y), 1)

    image.save("tree.bmp")


def part2():
    data = lines
    h = 103
    w = 101

    robots = []
    for row in data:
        x, y, vx, vy = map(int, re.findall(r"\-?\d+", row))
        robots.append(list((x, y, vx, vy)))

    facility = [[0 for x in range(w)] for y in range(h)]

    for robot in robots:
        p_x, p_y, v_x, v_y = robot
        facility[p_y][p_x] += 1

    i = 1
    while True:
        for j in range(len(robots)):
            p_x, p_y, v_x, v_y = robots[j]

            # remove current robot position
            facility[p_y][p_x] -= 1

            # calculate new robot position
            p_x = (p_x + v_x) % w
            p_y = (p_y + v_y) % h

            # update robot position
            robots[j] = [p_x, p_y, v_x, v_y]

            # record new robot position
            facility[p_y][p_x] += 1

        # if all robots in unique positions, found the tree
        if max([facility[y][x] for y in range(h) for x in range(w)]) == 1:
            break

        i += 1

    # create tree image file
    print_map(facility, w, h)
    print(i)  # print iteration count until tree
    ans2 = i
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=14, year=2024)
submit(ans2, part="b", day=14, year=2024)
