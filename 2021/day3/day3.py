from aocd import lines
from aocd import submit

data = lines

# utils
def to_base_ten(s):
    width = len(s)
    b10 = 0
    for i in range(0, width):
        b10 += int(s[i]) * 2 ** (width - 1 - i)
    return b10


# part 1

# gamma bit is most common in each col

length = len(data)
width = len(data[0])
gamma = ""
epsilon = ""
for i in range(0, width):
    num_1s = num_0s = 0
    for j in range(0, length):
        if data[j][i] == "1":
            num_1s += 1
        else:
            num_0s += 1
    g_bit = "1" if num_1s > num_0s else "0"
    e_bit = "0" if num_1s > num_0s else "1"
    gamma += g_bit
    epsilon += e_bit

e = to_base_ten(epsilon)
g = to_base_ten(gamma)

ans1 = e * g
print("ans1: %d" % ans1)


# submit(ans1, part="a", day=3, year=2021)

# part 2


def reducer(bin_arr, idx, param):
    length = len(bin_arr)

    # base case
    if len(bin_arr) == 1:
        num = to_base_ten(bin_arr[0])
        return num

    # find the most common value

    num_1s = num_0s = 0
    for j in range(0, length):
        if bin_arr[j][idx] == "1":
            num_1s += 1
        else:
            num_0s += 1
    common_bit = "1" if num_1s >= num_0s else "0"
    uncommon_bit = "0" if num_1s >= num_0s else "1"

    # remove any entry that doesnt start with correct bit (depends on param)
    if param == "oxy":
        reduced = [b for b in bin_arr if b[idx] == common_bit]

    if param == "co2":
        reduced = [b for b in bin_arr if b[idx] == uncommon_bit]

    # move to the next position
    idx += 1

    # recur
    return reducer(reduced, idx, param)


o = reducer(data, 0, "oxy")
c = reducer(data, 0, "co2")
ans2 = o * c
print("ans2: %d" % ans2)
# submit(ans2, part="b", day=3, year=2021)

# 00100, 01111, 00111, 00010, and 01010
