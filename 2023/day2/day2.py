import os
from xmlrpc.server import MultiPathXMLRPCServer
from aocd import lines, submit, get_data
import re


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def part1():
    constraints = dict(red=12, green=13, blue=14)

    def check_possible(rolls):
        for r in rolls:
            dice = re.findall(r"\d+ \w+", r)
            for d in dice:
                num, color = d.split(" ")
                if constraints[color] < int(num):
                    return False
        return True

    possible = []
    # data = test_data
    data = lines
    for idx, game in enumerate(data):
        game_id = 1 + idx
        rolls = game.split(";")
        p = check_possible(rolls)
        if p:
            possible.append(game_id)
    ans = sum(possible)
    submit(ans, part="a", day=2, year=2023)
    # ! CORRECT!


def part2():
    # data = test_data
    data = lines
    powers = []
    for game in data:
        rolls = game.split(";")
        maxes = dict(red=0, blue=0, green=0)
        for r in rolls:
            dice = re.findall(r"\d+ \w+", r)
            for d in dice:
                num, color = d.split(" ")
                maxes[color] = int(num) if int(num) > maxes[color] else maxes[color]
        powers.append(maxes["red"] * maxes["blue"] * maxes["green"])
    ans = sum(powers)
    submit(ans, part="b", day=2, year=2023)
    # ! CORRECT


# part1()
# part2()
