from aocd import lines
from aocd import submit


# part 1

depth = 0
pos = 0
for d in lines:
    direction, dist = d.split(" ")
    if direction == "down":
        depth += int(dist)
    if direction == "up":
        depth -= int(dist)
    if direction == "forward":
        pos += int(dist)

ans1 = depth * pos
print(ans1)
# submit(ans1, part="a", day=2, year=2021)


# part 2

depth = 0
pos = 0
aim = 0

for d in lines:
    direction, dist = d.split(" ")
    if direction == "down":
        aim -= int(dist)
    if direction == "up":
        aim += int(dist)
    if direction == "forward":
        pos += int(dist)
        depth += int(dist) * aim
depth = abs(depth)
ans2 = pos * depth
print(ans2)
# submit(ans2, part="b", day=2, year=2021)
