from aocd import lines, submit, get_data
import numpy as np

test_data = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


def part1():
    # data = test_data
    data = lines

    array = np.array([[c for c in s] for s in data])
    ys, xs = np.where(array == "O")
    coords = [(ys[i], xs[i]) for i in range(0, len(ys))]

    ans1 = 0
    for c in coords:
        y, x = c
        # move up as far as possible
        i = 1
        while array[y - i][x] not in ["O", "#"] and y - i > -1:
            i += 1
        i -= 1
        ans1 += len(array) - (y - i)
        array[y - i][x] = "O"
        if y - i != y:
            array[y][x] = "."

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    array = np.array([[c for c in s] for s in data])
    ans2 = 0
    seen = {}
    l = len(array)

    for cycle in range(1, 1000000000):
        for i in range(0, 4):
            ys, xs = np.where(array == "O")
            coords = [(ys[i], xs[i]) for i in range(0, len(ys))]
            ans2 = 0
            for c in coords:
                y, x = c
                # move up as far as possible
                i = 1
                while array[y - i][x] not in ["O", "#"] and y - i > -1:
                    i += 1
                i -= 1
                array[y - i][x] = "O"
                if y - i != y:
                    array[y][x] = "."
            array = np.rot90(array, k=1, axes=(1, 0))
            nys, nxs = np.where(array == "O")
            new_coords = [(nys[i], nxs[i]) for i in range(0, len(nys))]
        if new_coords not in seen.values():
            seen[cycle] = new_coords
        else:
            key = [i for i in seen if seen[i] == new_coords][0]
            period = cycle - key
            break
        
    iters = (1000000000 - key) % period
    last_key = key + iters
    coords = seen[last_key]
    ans2 = sum([l - y for (y,x) in coords])
    print(ans2)

    return ans2


ans1 = part1()
ans2 = part2()


# submit(ans1, part="a", day=14, year=2023) #! correct!
# submit(ans2, part="b", day=14, year=2023) #! correct!
