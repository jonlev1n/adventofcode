from aocd import lines, submit, get_data
import re
from z3 import Int, Solver

test_data = [
    "19, 13, 30 @ -2,  1, -2",
    "18, 19, 22 @ -1, -1, -2",
    "20, 25, 34 @ -2, -2, -4",
    "12, 31, 28 @ -1, -2, -1",
    "20, 19, 15 @  1, -5, -3",
]


def part1():
    # data = test_data
    # MIN = 7
    # MAX = 27
    data = lines
    MIN = 200000000000000
    MAX = 400000000000000

    PV = []

    ans1 = 0

    for row in data:
        n = re.findall(r"[-]?\d+", row)
        PV.append(list(map(int, n)))

    pairs = [[p1, p2] for idx, p1 in enumerate(PV) for p2 in PV[idx + 1 :]]

    for p1, p2 in pairs:
        p1x, p1y = p1[0:2]
        v1x, v1y = p1[3:5]
        p2x, p2y = p2[0:2]
        v2x, v2y = p2[3:5]

        # y = sx + c
        s1 = v1y / v1x
        s2 = v2y / v2x

        c1 = p1y - s1 * p1x
        c2 = p2y - s2 * p2x
        if (s1 - s2) != 0:
            x0 = (c2 - c1) / (s1 - s2)
            y0 = x0 * s1 + c1
            # check velocities to see if that is achievable
            x1r = (
                (MIN if p1x <= MIN else p1x, MAX)
                if v1x > 0
                else (MIN, MAX if p1x >= MAX else p1x)
            )
            y1r = (
                (MIN if p1y <= MIN else p1y, MAX)
                if v1y > 0
                else (MIN, MAX if p1y >= MAX else p1y)
            )
            x2r = (
                (MIN if p2x <= MIN else p2x, MAX)
                if v2x > 0
                else (MIN, MAX if p2x >= MAX else p2x)
            )
            y2r = (
                (MIN if p2y <= MIN else p2y, MAX)
                if v2y > 0
                else (MIN, MAX if p2y >= MAX else p2y)
            )
            if (
                x1r[0] <= x0 <= x1r[1]
                and x2r[0] <= x0 <= x2r[1]
                and y1r[0] <= y0 <= y1r[1]
                and y2r[0] <= y0 <= y2r[1]
            ):
                ans1 += 1

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    PV = []
    for row in data:
        n = re.findall(r"[-]?\d+", row)
        PV.append(list(map(int, n)))

    x, y, z, dx, dy, dz = Int("x"), Int("y"), Int("z"), Int("dx"), Int("dy"), Int("dz")
    times = [Int(f"T{i}") for i in range(3)]

    solver = Solver()
    for i in range(0, 3):
        x_i, y_i, z_i, dx_i, dy_i, dz_i = PV[i]
        solver.add(x + times[i] * dx - x_i - times[i] * dx_i == 0)
        solver.add(y + times[i] * dy - y_i - times[i] * dy_i == 0)
        solver.add(z + times[i] * dz - z_i - times[i] * dz_i == 0)

    solver.check()
    model = solver.model()
    ans2 = model.eval(x + y + z)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=24, year=2023) #! correct!
submit(ans2, part="b", day=24, year=2023)
