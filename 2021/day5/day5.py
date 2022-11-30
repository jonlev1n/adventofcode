from aocd import lines
import numpy as np
from aocd import submit

# data = [
#     "0,9 -> 5,9",
#     "8,0 -> 0,8",
#     "9,4 -> 3,4",
#     "2,2 -> 2,1",
#     "7,0 -> 7,4",
#     "6,4 -> 2,0",
#     "0,9 -> 2,9",
#     "3,4 -> 1,4",
#     "0,0 -> 8,8",
#     "5,5 -> 8,2",
# ]

data = lines

max_num = 0
for idx, coords in enumerate(data):
    data[idx] = [int(num) for num in coords.replace(" -> ", ",").split(",")]
    if max(data[idx]) > max_num:
        max_num = max(data[idx]) + 1

# part 1
# weed out non straight lines
def p1():
    straight_lines = [p for p in data if p[0] == p[2] or p[1] == p[3]]
    field = np.zeros((max_num, max_num), int)
    for line in straight_lines:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]

        low_bound = min([y1, y2]) if x1 == x2 else min(x1, x2)
        hi_bound = max([y1, y2]) if x1 == x2 else max(x1, x2)
        r = range(low_bound, hi_bound + 1)

        for q in r:
            if x1 == x2:
                field[x1][q] += 1
            if y1 == y2:
                field[q][y1] += 1

    return len(field[field >= 2])


def p2():
    field = np.zeros((max_num, max_num), int)
    for line in data:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]

        low_bound = min([y1, y2]) if x1 == x2 else min(x1, x2)
        hi_bound = max([y1, y2]) if x1 == x2 else max(x1, x2)
        low_x = min(x1, x2)
        low_y = min(y1, y2)
        high_x = max(x1, x2)
        high_y = max(y1, y2)
        r = range(low_bound, hi_bound + 1)
        if x1 != x2 and y1 != y2:
            x_range = (
                range(low_x, high_x + 1) if x2 > x1 else range(high_x, low_x - 1, -1)
            )
            y_range = (
                range(low_y, high_y + 1) if y2 > y1 else range(high_y, low_y - 1, -1)
            )

        for idx, q in enumerate(r):
            if x1 == x2:
                field[q][x1] += 1
            elif y1 == y2:
                field[y1][q] += 1
            elif x1 != x2 and y1 != y2:
                field[y_range[idx]][x_range[idx]] += 1

    return len(field[field >= 2])


ans1 = p1()
ans2 = p2()
# print(ans1)
print(ans2)
# submit(ans1, part="a", day=5, year=2021)
submit(ans2, part="b", day=5, year=2021)
