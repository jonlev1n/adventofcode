from aocd import lines, submit, get_data


test_data = [
    "#####",
    ".####",
    ".####",
    ".####",
    ".#.#.",
    ".#...",
    ".....",
    "",
    "#####",
    "##.##",
    ".#.##",
    "...##",
    "...#.",
    "...#.",
    ".....",
    "",
    ".....",
    "#....",
    "#....",
    "#...#",
    "#.#.#",
    "#.###",
    "#####",
    "",
    ".....",
    ".....",
    "#.#..",
    "###..",
    "###.#",
    "###.#",
    "#####",
    "",
    ".....",
    ".....",
    ".....",
    "#....",
    "#.#..",
    "#.#.#",
    "#####",
]


def part1():
    # data = test_data
    data = lines

    keys = []
    locks = []
    for i in range(0, len(data), 8):
        if all([v == "#" for v in data[i]]):
            n = []
            for x in range(5):
                for y in range(i, i + 7):
                    if data[y][x] == ".":
                        n.append((y - 1) % 8)
                        break

            locks.append(n)
        else:
            n = []
            for x in range(5):
                for y in range(i, i + 7):
                    if data[y][x] == "#":
                        n.append((6 - y) % 8)
                        break
            keys.append(n)

    ans1 = 0
    for key in keys:
        for lock in locks:
            s = [x + y for x, y in zip(key, lock)]
            if all([x < 6 for x in s]):
                ans1 += 1

    print(ans1)
    return ans1


def part2():
    data = test_data
    # data = lines

    ans2 = None
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=25, year=2024)
# submit(ans2, part="b", day=25, year=2024)
