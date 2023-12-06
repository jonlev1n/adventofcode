from aocd import lines, submit, get_data
import re


test_data = [
    "Time:      7  15   30", # in ms
    "Distance:  9  40  200", # in mm
]

def part1():
    # data = test_data
    data = lines
    [t,d] = data
    time = [int(num) for num in re.findall(r"\d+", t)]
    dist = [int(num) for num in re.findall(r"\d+", d)]

    # time is constraint
    ways2beat = 1
    for idx, t in enumerate(time):
        winning_dists = []
        for ms in range(1,t): # pad with one to make inclusive
            time_remaining = t - ms
            speed = ms
            d = speed * time_remaining
            if(d > dist[idx]):
                winning_dists.append(d)
        ways2beat *= len(winning_dists)

    return ways2beat

def part2():
    # data = test_data
    data = lines
    [t, d] = data
    time = int("".join([s for s in re.findall(r"\d+",t)]))
    dist = int("".join([s for s in re.findall(r"\d+",d)]))

    # count up from one until you beat the record the first time
    speed_l = 1
    while True:
        time_remaining = time - speed_l
        d = speed_l * time_remaining

        if d > dist:
            break
        speed_l += 1

    # then substract that value from the highest since answers are symmetrical
    ways2beat = time - 2*speed_l + 1
    return ways2beat

ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=6, year=2023) #! correct
# submit(ans2, part="b", day=6, year=2023) #! correct