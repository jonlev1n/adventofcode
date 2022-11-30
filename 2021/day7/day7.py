from aocd import lines
from aocd import submit

test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


# data = test_data
data = [int(x) for x in lines[0].split(",")]


fuel = dict()

# data = test_data

# part 1
# for a in data:
#     fuel[a] = sum(abs(a - b) for b in data)

# ans1 = min(fuel.values())

# print(ans1)
# submit(ans1, part="a", day=7, year=2021)

# part 2
for a in range(0, max(data) + 1):
    fuel[a] = sum((abs(a - b) * (abs(a - b) + 1)) / 2 for b in data)

ans2 = int(min(fuel.values()))
print(ans2)
submit(ans2, part="b", day=7, year=2021)
