from aocd import lines, submit, get_data
import numpy as np


test_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def part1():
    # data = test_data
    data = lines
    arr = [[".", ".", "."] + [x for x in row] + [".", ".", "."] for row in data]
    p = ["." for i in range(0, len(arr[0]))]
    arr.insert(0, p)
    arr.insert(0, p)
    arr.insert(0, p)
    arr.append(p)
    arr.append(p)
    arr.append(p)
    arr = np.array(arr)
    coords = np.where(arr == "X")
    ans1 = 0
    for i in range(0, len(coords[0])):
        y = coords[0][i]
        x = coords[1][i]

        strs = []

        strs.append(arr[y + 1][x + 1] + arr[y + 2][x + 2] + arr[y + 3][x + 3])
        strs.append(arr[y + 1][x] + arr[y + 2][x] + arr[y + 3][x])
        strs.append(arr[y + 1][x - 1] + arr[y + 2][x - 2] + arr[y + 3][x - 3])
        strs.append(arr[y][x - 1] + arr[y][x - 2] + arr[y][x - 3])
        strs.append(arr[y - 1][x - 1] + arr[y - 2][x - 2] + arr[y - 3][x - 3])
        strs.append(arr[y - 1][x] + arr[y - 2][x] + arr[y - 3][x])
        strs.append(arr[y - 1][x + 1] + arr[y - 2][x + 2] + arr[y - 3][x + 3])
        strs.append(arr[y][x + 1] + arr[y][x + 2] + arr[y][x + 3])

        ans1 += strs.count("MAS")
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    arr = [[".", ".", "."] + [x for x in row] + [".", ".", "."] for row in data]
    p = ["." for i in range(0, len(arr[0]))]
    arr.insert(0, p)
    arr.insert(0, p)
    arr.insert(0, p)
    arr.append(p)
    arr.append(p)
    arr = np.array(arr)
    coords = np.where(arr == "A")
    ans2 = 0

    for i in range(0, len(coords[0])):
        y = coords[0][i]
        x = coords[1][i]

        s1 = arr[y - 1][x - 1] + arr[y][x] + arr[y + 1][x + 1]
        s2 = arr[y + 1][x - 1] + arr[y][x] + arr[y - 1][x + 1]

        if (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM"):
            ans2 += 1
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=4, year=2024)
submit(ans2, part="b", day=4, year=2024)
