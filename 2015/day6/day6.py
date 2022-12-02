from aocd import get_data, submit
import numpy as np
import re

def solve_a(input):
    # init grid
    grid = np.zeros((1000, 1000), dtype=int)

    for line in input:
        # parse
        bounds = re.findall(r'\d+', line)
        x1 = int(bounds[0])
        y1 = int(bounds[1])
        x2 = int(bounds[2])
        y2 = int(bounds[3])
        off = "off" in line
        on = "on" in line
        toggle = "toggle" in line

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 +1):
                if off:
                    grid[j][i] = 0
                if on:
                    grid[j][i] = 1
                if toggle:
                    grid[j][i] = 1 if grid[j][i] == 0 else 0
    num_on = np.count_nonzero(grid == 1)
    return num_on

def solve_b(input):
    # init grid
    grid = np.zeros((1000, 1000), dtype=int)

    for line in input:
        # parse
        bounds = re.findall(r'\d+', line)
        x1 = int(bounds[0])
        y1 = int(bounds[1])
        x2 = int(bounds[2])
        y2 = int(bounds[3])
        off = "off" in line
        on = "on" in line
        toggle = "toggle" in line

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if off:
                    grid[j][i] -= 1
                    grid[j][i] = 0 if grid[j][i] < 0 else grid[j][i]
                if on:
                    grid[j][i] += 1
                if toggle:
                    grid[j][i] += 2
    total = np.sum(grid)
    return total


data = get_data(day=6, year=2015)
ans1 = solve_a(data.splitlines())
submit(ans1, day=6, year=2015, part="a")
ans2 = solve_b(data.splitlines())
submit(ans2, day=6, year=2015, part="b")