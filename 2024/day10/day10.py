from aocd import lines, submit, get_data
import numpy as np


test_data = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]

# test_data = [
#     "1044944",
#     "2555855",
#     "3999799",
#     "4567654",
#     "1118113",
#     "1119442",
#     "4444401",
# ]


def part1():
    # data = test_data
    data = lines

    arr = [[-99] + [int(c) for c in row] + [-99] for row in data]
    p = [-99 for i in range(0, len(arr[0]))]
    arr.insert(0, p)
    arr.append(p)
    A = np.array(arr)
    coords = np.where(A == 0)
    ys = coords[0]
    xs = coords[1]
    starts = [(ys[i], xs[i]) for i in range(0, len(xs))]

    V = []
    for s in starts:
        Q = [s]
        y, x = s
        v = 0
        valid_paths = 0
        peaks = []
        while len(Q) > 0:
            while v != 9:
                y, x = s
                v = A[y][x]
                up = A[y - 1][x] - v == 1
                down = A[y + 1][x] - v == 1
                left = A[y][x - 1] - v == 1
                right = A[y][x + 1] - v == 1
                next_s = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
                directions = [up, down, left, right]
                count = directions.count(True)

                if count == 0:
                    # can't move, break
                    break
                elif count == 1:
                    # move without adding to queue
                    idx = directions.index(True)
                    s = next_s[idx]
                else:
                    # more than one direction, add to queue
                    idxs = [i for i, x in enumerate(directions) if x]
                    to_Q = [next_s[idx] for idx in idxs]
                    s = to_Q.pop(0)
                    Q += to_Q
            if v == 9:
                if s not in peaks:
                    peaks.append(s)
                    valid_paths += 1
            Q.pop(0)
            if len(Q) > 0:
                s = Q[0]
                y, x = s
                v = A[y][x]
        V.append(valid_paths)
    ans1 = sum(V)
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    arr = [[-99] + [int(c) for c in row] + [-99] for row in data]
    p = [-99 for i in range(0, len(arr[0]))]
    arr.insert(0, p)
    arr.append(p)
    A = np.array(arr)
    coords = np.where(A == 0)
    ys = coords[0]
    xs = coords[1]
    starts = [(ys[i], xs[i]) for i in range(0, len(xs))]

    V = []
    for s in starts:
        Q = [s]
        y, x = s
        v = 0
        valid_paths = 0
        peaks = []
        while len(Q) > 0:
            while v != 9:
                y, x = s
                v = A[y][x]
                up = A[y - 1][x] - v == 1
                down = A[y + 1][x] - v == 1
                left = A[y][x - 1] - v == 1
                right = A[y][x + 1] - v == 1
                next_s = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
                directions = [up, down, left, right]
                count = directions.count(True)

                if count == 0:
                    # can't move, break
                    break
                elif count == 1:
                    # move without adding to queue
                    idx = directions.index(True)
                    s = next_s[idx]
                else:
                    # more than one direction, add to queue
                    idxs = [i for i, x in enumerate(directions) if x]
                    to_Q = [next_s[idx] for idx in idxs]
                    s = to_Q.pop(0)
                    Q += to_Q
            if v == 9:
                valid_paths += 1
            Q.pop(0)
            if len(Q) > 0:
                s = Q[0]
                y, x = s
                v = A[y][x]
        V.append(valid_paths)
    ans2 = sum(V)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=10, year=2024)
submit(ans2, part="b", day=10, year=2024)
