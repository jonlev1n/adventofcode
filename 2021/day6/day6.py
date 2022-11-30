from aocd import submit
from aocd import lines

# init as a map
# lanternfish = {
#     0: 0,
#     1: 1,
#     2: 1,
#     3: 2,
#     4: 1,
#     5: 0,
#     6: 0,
#     7: 0,
#     8: 0,
# }
data = [int(n) for n in lines[0].split(",")]
print(data)
lanternfish = dict()
for age in range(9):
    lanternfish[age] = sum(fish == age for fish in data)


days = 256

for d in range(days):
    new_fish = lanternfish[0]
    for key in range(8):
        # rotate the values down
        if key != 6:
            lanternfish[key] = lanternfish[key + 1]
        else:
            lanternfish[key] = lanternfish[key + 1] + new_fish
    lanternfish[8] = new_fish


ans1 = sum(lanternfish.values())
print(ans1)
# submit(ans1, part="a", day=6, year=2021)
