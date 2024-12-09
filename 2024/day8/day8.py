from aocd import lines, submit, get_data


test_data = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]


def part1():
    # data = test_data
    data = lines

    d = {}
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c != ".":
                if c in d:
                    d[c].append((i, j))
                else:
                    d[c] = [(i, j)]

    maxY = len(data)
    maxX = len(data[0])
    antinodes = []
    for key in d.keys():
        points = d[key]
        for i in range(0, len(points)):
            points_copy = [p for p in points]
            t = points_copy.pop(i)
            diffs = [((t[0] - p[0]), (t[1] - p[1])) for p in points_copy]
            for p in diffs:
                m = (t[0] + p[0], t[1] + p[1])
                n = (t[0] - p[0], t[1] - p[1])
                if (
                    m not in points
                    and m[0] in range(0, maxY)
                    and m[1] in range(0, maxX)
                ):
                    antinodes.append(m)
                if (
                    n not in points
                    and n[0] in range(0, maxY)
                    and n[1] in range(0, maxX)
                ):
                    antinodes.append(n)

    ans1 = len(list(set(antinodes)))
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    d = {}
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c != ".":
                if c in d:
                    d[c].append((i, j))
                else:
                    d[c] = [(i, j)]

    maxY = len(data)
    maxX = len(data[0])
    antinodes = []
    for key in d.keys():
        points = d[key]
        for i in range(0, len(points)):
            points_copy = [p for p in points]
            t = points_copy.pop(i)
            diffs = [((t[0] - p[0]), (t[1] - p[1])) for p in points_copy]
            for p in diffs:
                m = (t[0] + p[0], t[1] + p[1])
                n = (t[0] - p[0], t[1] - p[1])
                while m[0] in range(0, maxY) and m[1] in range(maxX):
                    antinodes.append(m)
                    m = (m[0] + p[0], m[1] + p[1])
                while n[0] in range(0, maxY) and n[1] in range(maxX):
                    antinodes.append(n)
                    n = (n[0] - p[0], n[1] - p[1])

    ans2 = len(list(set(antinodes)))
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=8, year=2024)
submit(ans2, part="b", day=8, year=2024)
