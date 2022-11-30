import numpy as np

test_data = {"x": (20, 30), "y": (-10, -5)}
real = {"x": (128, 160), "y": (-142, -88)}

# d = test_data
d = real


def get_vx():
    # find x velocity such that (x*x+1)/2 = min velocity and max velocity
    # min_x = x^2 + x - 2*d["x"][0] == 0
    # (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    a = b = 1
    c = -2 * d["x"][0]
    r1 = [x for x in np.roots([a, b, c]) if x > 0][0]
    vx = int(np.ceil(r1))
    return vx


def part1():
    vx = (get_vx(), d["x"][1] + 1)
    a = []
    for x in range(vx[0], vx[1]):
        for y in range(-160, 160):
            p = (0, 0)
            new_vx = x
            new_vy = y
            while p[1] >= d["y"][0]:
                # check to see if in bound
                if p[0] in range(d["x"][0], d["x"][1] + 1) and p[1] in range(
                    d["y"][0], d["y"][1] + 1
                ):
                    # add x,y to a
                    a.append((x, y))
                    break
                # update position
                px = p[0]
                px += new_vx
                py = p[1]
                py += new_vy
                p = (px, py)
                # update velocity
                new_vx -= 1 if new_vx > 0 else new_vx
                new_vy -= 1

    # get the max y
    mvy = 0
    for p in a:
        mvy = p[1] if p[1] > mvy else mvy
    my = mvy * (1 + mvy) / 2
    # a = list(set(a))

    print(my)  # part 1
    print(len(a))  # part 2


part1()
