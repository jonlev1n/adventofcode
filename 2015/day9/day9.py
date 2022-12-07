import os
from aocd import lines, submit, get_data
import re, itertools

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input):
    cities = []
    dists = {}
    for line in input:
        res = re.findall(r"[\w]{3,}|[\d]+", line)
        if not res[0] in dists.keys():
            dists[res[0]] = {res[1]: int(res[2])}
        else:
            dists[res[0]] = {**dists[res[0]], res[1]: int(res[2])}
        if not res[1] in dists.keys():
            dists[res[1]] = {res[0]: int(res[2])}
        else:
            dists[res[1]] = {**dists[res[1]], res[0]: int(res[2])}

        for i in range(0, 2):
            if res[i] not in cities:
                cities.append(res[i])

    permutations = list(itertools.permutations(cities))
    min_dist = -1
    max_dist = 0
    for p in permutations:
        dist = 0
        for i in range(0, len(p) - 1):
            dist += dists[p[i]][p[i + 1]]
        if min_dist < 0 or dist < min_dist:
            min_dist = dist
        if dist > max_dist:
            max_dist = dist

    return min_dist, max_dist


data = get_data(day=9, year=2015)
ans1 = solve(data.splitlines())[0]
ans2 = solve(data.splitlines())[1]
submit(ans1, day=9, year=2015, part="a")
submit(ans2, day=9, year=2015, part="b")
