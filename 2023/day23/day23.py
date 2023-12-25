from aocd import lines, submit, get_data
from collections import defaultdict

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
Q = [[(0, 1)]]
C = []
LF = None
DEST = None


def get_last_fork(data):
    # start at last position
    cy, cx = (len(data) - 1, len(data[0]) - 2)
    c = (cy, cx)
    steps = [c]
    prev_c = None
    while True:
        cy, cx = c
        next_c = [
            (cy + dy, cx + dx)
            for (dy, dx) in D.values()
            if (
                cy + dy in range(0, len(data))
                and cx + dx in range(0, len(data[0]))
                and data[(cy + dy)][(cx + dx)] == "."
                and (cy + dy, cx + dx) not in steps
            )
        ]

        if len(next_c) > 1:
            return (cy, cx), prev_c

        else:
            prev_c = c
            c = next_c[0]
            steps.append(c)


def traverse(c, steps, data):
    while len(Q) > 0 and len:
        cy, cx = c
        p = data[cy][cx]
        if c == LF:
            next_c = [DEST]
        elif p in D.keys():
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
            Q.append(steps.copy())
            C.append(next_c[1])

        if all([c in steps for c in next_c]):
            S.append(steps)
            if len(Q) == 0 or len(C) == 0:
                break
            last_steps = Q.pop()
            last_c = C.pop()
            last_steps.append(last_c)
            return traverse(last_c, last_steps, data)
        else:
            c = next_c[0]
            steps.append(c)
    return S


def part1():
    data = test_data
    # data = lines

    sy, sx = (0, 1)
    steps = [(sy, sx)]

    S = traverse((sy, sx), steps, data)
    ans1 = max([len(s) for s in S]) - 1
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    data = [
        row.replace(">", ".").replace("<", ".").replace("^", ".").replace("v", ".")
        for row in data
    ]

    start = (
        1,
        1,
    )  # starting at second tile to prevent the search from going backwards and out of bounds
    target = (len(data) - 1, len(data[0]) - 2)

    # create graph where the nodes are the intersections of the grid
    graph = defaultdict(list)
    queue = [(start, start, {start, (0, 1)})]
    while queue:
        curr_xy, prev_node, visited = queue.pop()
        if curr_xy == target:
            final_node = prev_node
            final_steps = len(visited) - 1
            continue

        (x, y) = curr_xy
        neighbors = []
        for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (i, j) not in visited and data[i][j] != "#":
                neighbors.append((i, j))

        if len(neighbors) == 1:  # neither intersection nor dead end
            nxt_xy = neighbors.pop()
            queue.append((nxt_xy, prev_node, visited | {nxt_xy}))

        elif len(neighbors) > 1:  # found an intersection ( node)
            steps = len(visited) - 1
            if (curr_xy, steps) in graph[prev_node]:  # already been here
                continue
            graph[prev_node].append((curr_xy, steps))
            graph[curr_xy].append((prev_node, steps))
            while neighbors:  # start new paths from current node
                nxt_xy = neighbors.pop()
                queue.append((nxt_xy, curr_xy, {curr_xy, nxt_xy}))

    # traverse graph
    max_steps = 0
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == final_node:
            max_steps = max(steps, max_steps)
            continue
        for nxt, distance in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps + distance, visited | {nxt}))

    ans2 = max_steps + final_steps
    print(ans2)
    return ans2


# ans1 = part1()
ans2 = part2()


# uncomment these lines to submit
# submit(ans1, part="a", day=23, year=2023) #! correct!
submit(ans2, part="b", day=23, year=2023)
