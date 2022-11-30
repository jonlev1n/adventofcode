import copy, time
from functools import reduce
import operator
file = open("/Users/jonathanlevin/git/adventofcode2020/day13/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day13/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day13/test_input2.txt", "r")

lines = file.readlines()

def parse_ids(i):
    if i != 'x':
        return i

schedules = []
for i in range(0, len(lines), 2):
    ids = lines[i+1].split(",")
    ids = filter(parse_ids, ids)
    schedule = {"timestamp": int(lines[i].replace("\n", "")), "ids": ids }
    schedules.append(schedule)


def part1():
    for s in schedules:
        timestamp = s["timestamp"]
        ids = s["ids"]
        times = []
        for i in ids:
            bus_id = int(i)
            floor = math.floor(timestamp/bus_id)
            if floor == 0:
                times.append(bus_id)
            else:
                times.append(int(floor+1)*bus_id)
        min_bus_time = min(times)
        idx = times.index(min_bus_time)
        bus_id = ids[idx]
        wait_time = min_bus_time - timestamp
        print(bus_id)
        print(wait_time)
        ans = int(bus_id ) * int(wait_time)
    return ans

# p1 = part1()
# print(p1)

def part2():
    start_time = time.time()
    bus_ids = copy.deepcopy(map(int, schedules[0]["ids"]))
    offsets = []
    for bus_id in bus_ids:
        offset = lines[1].split(",").index(str(bus_id))
        offsets.append(offset)
    
    # chinese remainder theorem
    total = 0
    for i in range(0, len(bus_ids)):
        if offsets[i] == 0:
            b_i = 0
        else:
            b_i = bus_ids[i] - offsets[i]
        
        N_i = reduce(operator.mul, bus_ids, 1)/bus_ids[i]

        x_i = 1
        for j in range(1, bus_ids[i]):
            if (N_i * j) % bus_ids[i] == 1:
                x_i = j
                break
        
        total += b_i * N_i * x_i
    return (total % reduce(operator.mul, bus_ids, 1))




p2 = part2() 
print(p2)
