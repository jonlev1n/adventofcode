from aocd import lines, submit, get_data
from collections import deque


data = lines
y_len = len(data)
x_len = len(data[0])


def get_beams():
    beams = {}
    queue = [(">", 0, 0)]
    while len(queue) > 0:
        (dir, x, y) = queue.pop()
        if (x, y) not in beams:
            beams[(x, y)] = []
        if dir in beams[(x, y)]:
            continue
        beams[(x, y)].append(dir)

        moves = next_move(dir, data[y][x])
        for move in moves:
            a, b = new_position(x, y, move)
            if a in range(x_len) and b in range(y_len):
                queue.append((move, a, b))
    return beams


def get_max():
    max_energized = 0
    for x in range(x_len):
        energized = process_beam("v", x, 0)
        max_energized = max(max_energized, energized)

        energized = process_beam("^", x, y_len - 1)
        max_energized = max(max_energized, energized)

    for y in range(y_len):
        energized = process_beam(">", 0, y)
        max_energized = max(max_energized, energized)

        energized = process_beam("<", x_len - 1, y)
        max_energized = max(max_energized, energized)
    return max_energized


def process_beam(dir, x, y):
    beams = track_light_beams(dir, x, y)
    energized = len(beams)
    return energized


def track_light_beams(start_dir, start_x, start_y):
    beams = {}
    queue = [(start_dir, start_x, start_y)]
    while len(queue) > 0:
        (dir, x, y) = queue.pop()
        if (x, y) not in beams:
            beams[(x, y)] = []
        if dir in beams[(x, y)]:
            continue
        beams[(x, y)].append(dir)

        moves = next_move(dir, data[y][x])
        for move in moves:
            a, b = new_position(x, y, move)
            if a in range(x_len) and b in range(y_len):
                queue.append((move, a, b))
    return beams


def next_move(dir, mirror):
    if mirror == ".":
        return dir
    if mirror == "|":
        if dir in "v^":
            return dir
        else:
            return "v^"
    if mirror == "-":
        if dir in "><":
            return dir
        else:
            return "><"
    if mirror == "/":
        if dir == ">":
            return "^"
        if dir == "v":
            return "<"
        if dir == "<":
            return "v"
        if dir == "^":
            return ">"
    if mirror == "\\":
        if dir == ">":
            return "v"
        if dir == "v":
            return ">"
        if dir == "<":
            return "^"
        if dir == "^":
            return "<"
    return


def new_position(x, y, move):
    if move == ">":
        return x + 1, y
    if move == "<":
        return x - 1, y
    if move == "^":
        return x, y - 1
    if move == "v":
        return x, y + 1
    return


def part1():
    beams = get_beams()
    ans1 = len(beams)
    print(ans1)
    return ans1


def part2():
    ans2 = get_max()
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

submit(ans1, part="a", day=16, year=2023)
submit(ans2, part="b", day=16, year=2023)
