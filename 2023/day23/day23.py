from aocd import lines, submit, get_data


test_data = [
    "#.#####################",
    "#.......#########...###",
    "#######.#########.#.###",
    "###.....#.>.>.###.#.###",
    "###v#####.#v#.###.#.###",
    "###.>...#.#.#.....#...#",
    "###v###.#.#.#########.#",
    "###...#.#.#.......#...#",
    "#####.#.#.#######.#.###",
    "#.....#.#.#.......#...#",
    "#.#####.#.#.#########v#",
    "#.#...#...#...###...>.#",
    "#.#.#v#######v###.###v#",
    "#...#.>.#...>.>.#.###.#",
    "#####v#.#.###v#.#.###.#",
    "#.....#...#...#.#.#...#",
    "#.#########.###.#.#.###",
    "#...###...#...#...#.###",
    "###.###.#.###v#####v###",
    "#...#...#.#.>.>.#.>.###",
    "#.###.###.#.###.#.#v###",
    "#.....###...###...#...#",
    "#####################.#",
]

D = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


S = []
Q = []


def traverse(c, steps, data):
    cy, cx = c
    p = data[cy][cx]
    if p in D.keys():
        next_c = [(cy + D[p][0], cx + D[p][1])]
    else:
        next_c = [
            (cy + dy, cx + dx)
            for (dy, dx) in D.values()
            if (
                cy + dy in range(0, len(data))
                and cx + dx in range(0, len(data[0]))
                and data[(cy + dy)][(cx + dx)] in list(D.keys()) + ["."]
                and (cy + dy, cx + dx) not in steps
                and not (
                    data[(cy + dy)][(cx + dx)] in D.keys()
                    and (
                        dy + D[data[(cy + dy)][(cx + dx)]][0],
                        dx + D[data[(cy + dy)][(cx + dx)]][1],
                    )
                    == (0, 0)
                )
            )
        ]

    if len(next_c) > 1:
        Q.insert(0, steps.copy())

    if all([c in steps for c in next_c]):
        return steps
    else:
        for c in next_c:
            # steps = Q.pop()
            steps.append(c)
            # print("steps:", steps)
            print(c, next_c)
            return traverse(c, steps, data)


def part1():
    data = test_data
    # data = lines

    sy, sx = (0, 1)
    steps = [(sy, sx)]
    # ey, ex = (len(data) - 1, len(data) - 2)

    S = traverse((sy, sx), steps, data)
    print("S:", S)

    ans1 = None
    return ans1


def part2():
    data = test_data
    # data = lines

    ans2 = None
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=23, year=2023)
# submit(ans2, part="b", day=23, year=2023)
