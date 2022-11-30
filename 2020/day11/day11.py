import copy

file = open("/Users/jonathanlevin/git/adventofcode2020/day11/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day11/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day11/test_input2.txt", "r")
lines = file.readlines()

layout = []
for line in lines:
    layout.append([char for char in line if char != "\n"])

# for a given square (i,j) the surrounding square are up to 8 possibilities
def find_next_layout(layout):
    original_layout = copy.deepcopy(layout)
    # print(original_layout[-1])
    new_layout = [[0 for col in range(len(layout[0]))] for row in range(len(layout))]
    for i in range(len(original_layout)):
        for j in range(len(original_layout[0])):
            adjacents = []
            a_start = -1
            b_start = -1
            if i == 0:
                a_start = 0
            if j == 0:
                b_start = 0
            for a in range(a_start, 2):
                for b in range(b_start, 2):
                    if a == 0 and b == 0:
                        pass
                    else:
                        try:
                            adj = original_layout[i + a][j + b]
                            adjacents.append(adj)
                        except:
                            pass
            # print(adjacents)
                
            if original_layout[i][j] == 'L' and '#' not in adjacents:
                new_layout[i][j] = '#'
            elif layout[i][j] == '#' and adjacents.count('#') >= 4:
                new_layout[i][j] = 'L'
            else:
                new_layout[i][j] = original_layout[i][j]
            
    return new_layout

def steadyState(layout):
    cur_layout = layout
    next_layout = find_next_layout(cur_layout)

    while (cur_layout != next_layout):
        cur_layout = copy.deepcopy(next_layout)
        tmp_layout = find_next_layout(cur_layout)
        next_layout = copy.deepcopy(tmp_layout)

    occupied_seats = 0
    for row in cur_layout:
        occupied_seats += row.count('#')
    return occupied_seats
    

           

occ = steadyState(layout)
print(occ)


def part2(layout):
    original_layout = copy.deepcopy(layout)
    # print(original_layout[-1])
    new_layout = [[0 for col in range(len(layout[0]))]
                  for row in range(len(layout))]
    for i in range(len(original_layout)):
        for j in range(len(original_layout[0])):
            adjacents = []
            a_start = -1
            b_start = -1
            if i == 0:
                a_start = 0
            if j == 0:
                b_start = 0
            for a in range(a_start, 2):
                for b in range(b_start, 2):
                    if a == 0 and b == 0:
                        pass
                    else:
                        try:
                            aa = a
                            bb = b
                            adj = original_layout[i + a][j + b]
                            # continue the search in the same direction
                            while adj != "#" and adj != 'L':
                                print("looping")
                                if a > 0:
                                    aa += 1
                                if b > 0:
                                    bb += 1
                                if a < 0:
                                    aa -= 1
                                if b < 0:
                                    bb -= 1
                                # break if we get too big
                                if i + aa < 0 or i + aa > len(original_layout):
                                    break
                                if j + bb < 0  or j + bb > len(original_layout[0]):
                                    break
                                adj = original_layout[i + aa][j + bb]
                            adjacents.append(adj)
                        except:
                            pass
                        if a < a_start:
                            a = a_start 
                        if b < b_start:
                            b = b_start 

            if original_layout[i][j] == 'L' and '#' not in adjacents:
                new_layout[i][j] = '#'
            elif layout[i][j] == '#' and adjacents.count('#') >= 5:
                new_layout[i][j] = 'L'
            else:
                new_layout[i][j] = original_layout[i][j]

    return new_layout


def steadyStateP2(layout):
    cur_layout = layout
    next_layout = part2(cur_layout)

    while (cur_layout != next_layout):
        cur_layout = copy.deepcopy(next_layout)
        tmp_layout = part2(cur_layout)
        next_layout = copy.deepcopy(tmp_layout)

    print(cur_layout)
    occupied_seats = 0
    for row in cur_layout:
        occupied_seats += row.count('#')
    return occupied_seats

occp2 = steadyStateP2(layout)
print(occp2)
