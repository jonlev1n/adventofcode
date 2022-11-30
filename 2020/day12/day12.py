import copy, time
file = open("/Users/jonathanlevin/git/adventofcode2020/day12/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day12/test_input.txt", "r")

lines = file.readlines()

directions = []
for line in lines:
    direction = {"movement": line[0], "value": int(line[1:].replace('\n', ''))}
    directions.append(direction)
    
def part1():
    start_time = time.time()
    angle = east = west = north = south = 0

    for d in directions:
        # calculate new angle
        if d["movement"] == 'R':
            angle = (angle + d["value"]) % 360
        elif d["movement"] == 'L':
            angle = (angle - d["value"]) % 360
        # else the angle doesnt change

        if d["movement"] == 'F':
            # have to see the angle we're at
            if angle == 0:
                east += d["value"]
            elif angle == 90:
                south += d["value"]
            elif angle == 180:
                west += d["value"]
            elif angle == 270:
                north += d["value"]
        else:
            if d["movement"] == 'N':
                north += d["value"]
            elif d["movement"] == 'E':
                east += d["value"]
            elif d["movement"] == 'S':
                south += d["value"]
            elif d["movement"] == 'W':
                west += d["value"]
        
    # manhattan distance is abs(east - west) + abs(north - south)
    manhattan = abs(east - west) + abs(north - south)
    print("------ Part 1 ran in %d s ------" % (time.time() - start_time))
    return manhattan

m = part1()
print(m)

def part2():
    start_time = time.time()
    # waypoint is n, e, s, w
    waypoint = [1, 10, 0, 0]
    east = west = north = south = 0
    for d in directions:
        if d["movement"] == 'R':
            # rotate waypoint clockwise 
            # for every 90 deg east becomes south, south becomes west, west becomes north, north becomes east
            shift = (d["value"] % 360) / 90
            tmp_waypoint = copy.deepcopy(waypoint)
            for i in range(0, 4):
                new_i = (i + shift) % 4
                waypoint[new_i] = tmp_waypoint[i]
        elif d["movement"] == 'L':
            # rotate waypoint counterclockwise
            shift = (d["value"] % 360) / 90
            tmp_waypoint = copy.deepcopy(waypoint)
            for i in range(0, 4):
                new_i = (i - shift) % 4
                waypoint[new_i] = tmp_waypoint[i]
        elif d["movement"] == 'N':
            waypoint[0] += d["value"]
        elif d["movement"] == 'E':
            waypoint[1] += d["value"]
        elif d["movement"] == 'S':
            waypoint[2] += d["value"]
        elif d["movement"] == 'W':
            waypoint[3] += d["value"]
        elif d["movement"] == 'F':
            north += waypoint[0] * d["value"]
            east += waypoint[1] * d["value"]
            south += waypoint[2] * d["value"]
            west += waypoint[3] * d["value"]
    
    manhattan = abs(east - west) + abs(north - south)
    print("------ Part 2 ran in %d s ------" % (time.time() - start_time))
    return manhattan

m2 = part2()
print(m2)
