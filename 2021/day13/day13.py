from aocd import lines
import numpy as np

test_data = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

# data = test_data
data = lines

coords = []
folds = []
max_x = 0
max_y = 0
for d in data:
    if len(d) > 0:
        if d[0].isnumeric():
            x, y = d.split(",")
            x = int(x)
            y = int(y)
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y
            coords.append((x, y))
        else:
            axis, value = d.split("=")
            axis = axis[-1]
            value = int(value)
            folds.append({axis: value})

# print(folds)

# create initial grid using 1s and 0s
a = np.zeros((max_y + 1, max_x + 1), dtype=int)
for j, i in coords:
    a[i][j] = 1

print(folds)

# fold

# if axis is y go down (rows) if x go right (cols)
for f in folds:
    axis = list(f.keys()).pop()
    value = f[axis]

    # after every fold recalculate dims
    max_y, max_x = a.shape

    if axis == "y":
        delta = max_y - 1 - value
        start = value - delta
        i = start
        for x in range(max_y - 1, value, -1):
            for j in range(0, max_x):
                if a[x][j] == 1:
                    a[i][j] = 1
            i += 1

        # cut off the bottom part
        a = a[0:value, :]

    if axis == "x":
        delta = max_x - 1 - value
        start = value - delta
        for i in range(0, max_y):
            j = start
            for x in range(max_x - 1, value, -1):
                if a[i][x] == 1:
                    a[i][j] = 1
                j += 1

        # cut off the right part
        a = a[:, 0:value]

    # break  # part 1 is just the first fold

# ans1 = np.count_nonzero(a > 0)
# print(ans1)

print(a)
