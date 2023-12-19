from aocd import lines, submit, get_data
from math import prod
from operator import lt, gt
import portion as P
from copy import deepcopy

test_data = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
    "",
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}",
]


def get_key(r, x, m, a, s):
    R = r.split(",")
    for i in R:
        A = i.split(":")
        if len(A) > 1:
            [expr, val] = A
            if eval(expr):
                return val
            else:
                continue
        else:
            return A[0]


def part1():
    # data = test_data
    data = lines

    idx = data.index("")
    R = data[0:idx]
    C = data[idx + 1 :]
    rules = {}

    # generate the ruleset
    for r in R:
        key, val = r.split("{")
        rules[key] = val.replace("}", "")

    ans1 = 0
    for c in C:
        c = c.replace("{", "").replace("}", "").split(",")

        x = int(c[0].split("=")[1])
        m = int(c[1].split("=")[1])
        a = int(c[2].split("=")[1])
        s = int(c[3].split("=")[1])

        K = "in"
        while K not in ["A", "R"]:
            r = rules[K]
            K = get_key(r, x, m, a, s)
            if K == "A":
                ans1 += x + m + a + s

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    idx = data.index("")
    R = data[0:idx]
    rules = {}

    # generate the ruleset
    for r in R:
        key, val = r.split("{")
        rules[key] = val.replace("}", "")

    def get_sols(K, bounds):
        f = rules[K]
        count = 0

        for ff in f.split(","):
            ff_parts = ff.split(":")
            if len(ff_parts) == 2:
                if_, then = ff_parts
                c = if_[0]
                o = lt if if_[1] == "<" else gt
                i = int(if_[2:])

                if then != "R":
                    then_bounds = deepcopy(bounds)
                    then_bounds[c] &= (
                        P.openclosed(i, then_bounds[c].upper)
                        if o == gt
                        else P.closedopen(then_bounds[c].lower, i)
                    )
                    if any(b.empty for b in then_bounds.values()):
                        break

                    if then == "A":
                        count += prod(
                            len(list(P.iterate(b, step=1)))
                            for b in then_bounds.values()
                        )
                    else:
                        count += get_sols(then, then_bounds)

                if o == lt:
                    bounds[c] &= P.closed(i, bounds[c].upper)
                else:
                    bounds[c] &= P.closed(bounds[c].lower, i)

                if any(b.empty for b in bounds.values()):
                    break
            else:
                label = ff_parts[0]
                if label != "R":
                    if label == "A":
                        count += prod(
                            len(list(P.iterate(b, step=1))) for b in bounds.values()
                        )
                    else:
                        count += get_sols(label, bounds)

        return count

    K = "in"
    bounds = {v: P.closed(1, 4000) for v in "xmas"}
    ans2 = get_sols(K, bounds)

    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=19, year=2023) # ! correct!
# submit(ans2, part="b", day=19, year=2023) # ! correct!
