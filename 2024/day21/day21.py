from aocd import lines, submit, get_data


from typing import Any
import os
from time import perf_counter_ns
from itertools import pairwise, permutations
from functools import cache


def profiler(method):

    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter_ns()
        ret = method(*args, **kwargs)
        stop_time = perf_counter_ns() - start_time
        time_len = min(9, ((len(str(stop_time)) - 1) // 3) * 3)
        time_conversion = {
            9: "seconds",
            6: "milliseconds",
            3: "microseconds",
            0: "nanoseconds",
        }
        print(
            f"Method {method.__name__} took : {
              stop_time / (10**time_len)} {time_conversion[time_len]}"
        )
        return ret

    return wrapper_method


@cache
def get_deltas(a, b):
    if a == b:
        return 0, 0

    if len(set(a + b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3
    bx, by = keypad.index(b) % 3, keypad.index(b) // 3

    return bx - ax, by - ay


@cache
def is_valid_path(a, b, path):
    if len(set(a + b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3

    deltas = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}

    for p in path:
        dx, dy = deltas[p]
        ax += dx
        ay += dy

        if ax < 0 or ax >= 3 or ay < 0 or ay >= len(keypad) // 3:
            return False

        if keypad[ay * 3 + ax] == "X":
            return False
    return True


@cache
def get_all_paths(a, b):
    dx, dy = get_deltas(a, b)

    cx = "<" if dx < 0 else ">"
    cy = "^" if dy < 0 else "v"

    nx = cx * abs(dx) + cy * abs(dy)
    possible = []
    for p in permutations(nx):
        if is_valid_path(a, b, p):
            possible.append("".join(p) + "A")

    return possible


@cache
def get_min_cost(seq, depth):
    ret = 0
    seq = "A" + seq
    for a, b in pairwise(seq):
        ps = get_all_paths(a, b)
        if depth == 0:
            ret += min(len(p) for p in ps)
        else:
            ret += min(get_min_cost(p, depth - 1) for p in ps)
    return ret


@profiler
def part1():
    # data = test_data
    data = lines

    t = 0
    for seq in data:
        t += get_min_cost(seq, 2) * int(seq.replace("A", ""))

    print(t)
    return t


@profiler
def part2():
    # data = test_data
    data = lines
    t = 0
    for seq in data:
        t += get_min_cost(seq, 25) * int(seq.replace("A", ""))

    print(t)
    return t


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=21, year=2024)
submit(ans2, part="b", day=21, year=2024)
