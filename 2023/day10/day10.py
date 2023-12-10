import math
from aocd import lines, submit, get_data
import re


test_data = [
    "7-F7-",
    ".FJ|7",
    "SJLL7",
    "|F--J",
    "LJ.LJ",
]


def get_starting_idx(data):
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if "S" in col:
                start_idx = (i, j)
                return start_idx
            else:
                continue


# function to find the next piece of pipe
#      F|7
#   LF- x -7J
#      L|J
def get_next_idx(current_idx, data):
    y, x = current_idx
    coords = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]  # 4 values
    key = data[y][x]

    valid = {
        (y - 1, x): "F|7",
        (y + 1, x): "L|J",
        (y, x - 1): "LF-",
        (y, x + 1): "-7J",
    }

    key2coords = {
        "|": [coords[0], coords[1]],
        "-": [coords[2], coords[3]],
        "L": [coords[0], coords[3]],
        "J": [coords[0], coords[2]],
        "7": [coords[2], coords[1]],
        "F": [coords[1], coords[3]],
    }

    if key == "S":
        connected = []
        for c in coords:
            y2, x2 = c
            if y2 in range(0, len(data)) and x2 in range(0, len(data[0])):
                # check to see if those are valid
                if data[y2][x2] in valid[(y2, x2)]:
                    connected.append((y2, x2))
            else:
                continue
    else:
        connected = key2coords[key]

    return connected


def loop(data):
    # initialize
    start_idx = get_starting_idx(data)
    # track where we've been
    visited = [start_idx]

    current_idx = start_idx  # init
    step = 0
    # loop here
    while True:
        next_idxs = get_next_idx(current_idx, data)
        if all([c in visited for c in next_idxs]):
            break

        # select first idx not visted
        for c in next_idxs:
            if c not in visited:
                next_idx = c
                break
        visited.append(next_idx)
        current_idx = next_idx
    return visited


def part1():
    # data = test_data
    data = lines
    visited = loop(data)
    furthest = math.ceil(len(visited) / 2)
    print(furthest)
    return furthest


test_data_2 = [
    # "..........",
    # ".S------7.",
    # ".|F----7|.",
    # ".||OOOO||.",
    # ".||OOOO||.",
    # ".|L-7F-J|.",
    # ".|II||II|.",
    # ".L--JL--J.",
    # "..........",
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJ7F7FJ-",
    "L---JF-JLJ.||-FJLJJ7",
    "|F|F-JF---7F7-L7L|7|",
    "|FFJF7L7F-JF7|JL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L",
    #     ".F----7F7F7F7F-7....",
    #     ".|F--7||||||||FJ....",
    #     ".||.FJ||||||||L7....",
    #     "FJL7L7LJLJ||LJ.L-7..",
    #     "L--J.L7...LJS7F-7L7.",
    #     "....F-J..F7FJ|L7L7L7",
    #     "....L7.F7||L7|.L7L7|",
    #     ".....|FJLJ|FJ|F7|.LJ",
    #     "....FJL-7.||.||||...",
    #     "....L---J.LJ.LJLJ...",
]


def part2():
    # data = test_data_2
    data = lines

    visited = loop(data)
    for y in range(0, len(data)):
        s = data[y]
        s_list = list(s)
        for x in range(0, len(data[0])):
            if (y, x) not in visited:
                s_list[x] = "."
        s = "".join(s_list)
        data[y] = s

    # convert data to actual list
    for idx, row in enumerate(data):
        data[idx] = [c for c in row]

    # flood fill dots with O on outside
    while True:
        changes_made = 0
        for y in range(0, len(data)):
            for x in range(0, len(data[0])):
                if (
                    x == 0 or y == 0 or x == len(data[0]) - 1 or y == len(data) - 1
                ) and data[y][x] == ".":
                    data[y][x] = "O"
                    changes_made += 1
                else:
                    adj = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
                    if data[y][x] == "." and any(
                        [data[y2][x2] == "O" for (y2, x2) in adj]
                    ):
                        data[y][x] = "O"
                        changes_made += 1
        if changes_made == 0:
            break

    # convert back to strings
    data = ["".join(row) for row in data]
    inside = 0
    for row in data:
        # visual inspection tells me S needs to be a 7
        s = row.replace("O", "")
        nots = re.findall(r"([^.]+)", s)
        dots = re.findall(r"([.]+)", s)

        for idx, i in enumerate(dots):
            l_str = nots[idx]
            r_str = nots[idx + 1]

            # replace for parity
            l_str = re.sub(r"F-*7|L-*J", "", l_str)
            r_str = re.sub(r"F-*7|L-*J", "", r_str)
            l_str = re.sub(r"F-*J|L-*7", "|", l_str)
            r_str = re.sub(r"F-*J|L-*7", "|", r_str)

            if len(l_str) % 2 != 0 or len(r_str) % 2 != 0:
                inside += len(i)

    print(inside + 1)
    return inside + 1


# ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=10, year=2023) #! correct!
# submit(ans2, part="b", day=10, year=2023) #! correct!
