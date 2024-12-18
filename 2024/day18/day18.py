from aocd import lines, submit, get_data
import numpy as np
from queue import Queue


test_data = [
    "5,4",
    "4,2",
    "4,5",
    "3,0",
    "2,1",
    "6,3",
    "2,4",
    "1,5",
    "0,6",
    "3,3",
    "2,6",
    "5,1",
    "1,2",
    "5,5",
    "2,5",
    "6,5",
    "1,4",
    "0,4",
    "6,4",
    "1,1",
    "6,1",
    "1,0",
    "0,5",
    "1,6",
    "2,0",
]


def bfs_shortest_path(grid, start, goal):
    rows, cols = grid.shape
    queue = Queue()
    queue.put((start, [start]))
    visited = set()
    visited.add(start)

    while not queue.empty():
        (current, path) = queue.get()
        x, y = current

        if current == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and grid[nx, ny] == 0
                and (nx, ny) not in visited
            ):
                queue.put(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None


def part1():
    # data = test_data
    data = lines

    grid = np.zeros((71, 71), dtype=int)

    for i, row in enumerate(data):
        x, y = map(int, row.split(","))
        grid[x, y] = 1

        if i == 1024:
            path = bfs_shortest_path(grid, (0, 0), (70, 70))
            return len(path) - 1


def part2():
    # data = test_data
    data = lines

    grid = np.zeros((71, 71), dtype=int)

    for i, row in enumerate(data):
        x, y = map(int, row.split(","))
        grid[x, y] = 1

        if i > 1024:
            path = bfs_shortest_path(grid, (0, 0), (70, 70))
            if not path:
                print(x, y)
                return "%d,%d" % (x, y)


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=18, year=2024)
submit(ans2, part="b", day=18, year=2024)
