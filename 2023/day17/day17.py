from aocd import lines, submit, get_data
import heapq


test_data = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]


def part1():
    # data = test_data
    data = lines

    D = [[int(c) for c in row] for row in data]
    H = len(D)
    W = len(D[0])
    Q = [(0, 0, 0, -1, -1)]
    G = {}
    while Q:
        dist, r, c, dir_, indir = heapq.heappop(Q)
        if (r, c, dir_, indir) in G:
            # assert dist >= D[(r,c,dir_,indir)]
            continue
        G[(r, c, dir_, indir)] = dist
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            rr = r + dr
            cc = c + dc
            new_dir = i
            new_indir = 1 if new_dir != dir_ else indir + 1

            isnt_reverse = (new_dir + 2) % 4 != dir_

            isvalid = new_indir <= 3

            if 0 <= rr < H and 0 <= cc < W and isnt_reverse and isvalid:
                cost = int(D[rr][cc])
                heapq.heappush(Q, (dist + cost, rr, cc, new_dir, new_indir))

    ans1 = float("inf")
    for (r, c, _, _), v in G.items():
        if r == H - 1 and c == W - 1:
            ans1 = min(ans1, v)
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    D = [[int(c) for c in row] for row in data]
    H = len(D)
    W = len(D[0])
    Q = [(0, 0, 0, -1, -1)]
    G = {}
    while Q:
        dist, r, c, dir_, indir = heapq.heappop(Q)
        if (r, c, dir_, indir) in G:
            # assert dist >= D[(r,c,dir_,indir)]
            continue
        G[(r, c, dir_, indir)] = dist
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            rr = r + dr
            cc = c + dc
            new_dir = i
            new_indir = 1 if new_dir != dir_ else indir + 1

            isnt_reverse = (new_dir + 2) % 4 != dir_

            isvalid = new_indir <= 10 and (new_dir == dir_ or indir >= 4 or indir == -1)

            if 0 <= rr < H and 0 <= cc < W and isnt_reverse and isvalid:
                cost = int(D[rr][cc])
                heapq.heappush(Q, (dist + cost, rr, cc, new_dir, new_indir))

    ans2 = float("inf")
    for (r, c, _, _), v in G.items():
        if r == H - 1 and c == W - 1:
            ans2 = min(ans2, v)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

submit(ans1, part="a", day=17, year=2023)
submit(ans2, part="b", day=17, year=2023)
