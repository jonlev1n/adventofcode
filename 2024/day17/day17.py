from aocd import lines, submit
import re


a = int(re.findall(r"\d+", lines[0])[0])
b = int(re.findall(r"\d+", lines[1])[0])
c = int(re.findall(r"\d+", lines[2])[0])
prog = [int(n) for n in re.findall(r"\d+", lines[4])]


def part1(prog, a):
    ip, b, c, out = 0, 0, 0, []
    while ip >= 0 and ip < len(prog):
        lit, combo = prog[ip + 1], [0, 1, 2, 3, a, b, c, 99999][prog[ip + 1]]
        match prog[ip]:
            case 0:
                a = int(a / 2**combo)  # adv
            case 1:
                b = b ^ lit  # bxl
            case 2:
                b = combo % 8  # bst
            case 3:
                ip = ip if a == 0 else lit - 2  # jnz
            case 4:
                b = b ^ c  # bxc
            case 5:
                out.append(combo % 8)  # out
            case 6:
                b = int(a / 2**combo)  # bdv
            case 7:
                c = int(a / 2**combo)  # cdv
        ip += 2
    ans1 = out
    print(ans1)
    return ans1


print("Part 1:", ",".join(str(n) for n in part1(prog, a)))

target = prog[::-1]


def part2(a=0, depth=0):
    if depth == len(target):
        return a
    for i in range(8):
        output = part1(prog, a * 8 + i)
        if output and output[0] == target[depth]:
            if result := part2((a * 8 + i), depth + 1):
                ans2 = result
                print("Part 2:", ans2)
                return ans2
    return 0


ans1 = part1(prog, a)
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=17, year=2024)
submit(ans2, part="b", day=17, year=2024)
