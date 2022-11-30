import copy
import time
import re
import math
file = open("/Users/jonathanlevin/git/adventofcode2020/day17/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day17/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day17/test_input2.txt", "r")

active_cubes3d = []
active_cubes4d = []
grid3d = []
grid4d = []
lines = file.read().splitlines()
x = 0
for line in lines:
    y = 0
    for cube in line:
        coord3d = [x,y,0]
        coord4d = [x,y,0,0]
        grid3d.append(coord3d)
        grid4d.append(coord4d)
        if cube == '#':
            active_cubes3d.append(coord3d)
            active_cubes4d.append(coord4d)
        
        y += 1
    x += 1

print(active_cubes3d)

# print("t= 0, active: %s" % active_cubes)
# print(grid)
# if a coordinate is not in inital_active it is inactive

def part1(n):
    start_grid = copy.deepcopy(grid3d)
    for i in range(0, n):
        next_grid = []
        for cube in start_grid:
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    for z in range(-1,2,1):
                        if not [cube[0] + x, cube[1] + y, cube[2] + z] in next_grid:
                            next_grid.append(([cube[0] + x, cube[1] + y, cube[2] + z]))
        start_grid = copy.deepcopy(next_grid)
        cubes_to_add = []
        cubes_to_remove = []
        print(next_grid)

        for cube in next_grid:
            neighbors = []
            # print(cube)
            an = 0
            for ac in active_cubes3d:
                if ac == cube:
                    pass
                elif abs(ac[0] - cube[0]) < 2 and abs(ac[1] - cube[1]) < 2 and abs(ac[2] - cube[2]) < 2:
                    an += 1
            if(cube[2] == 0):
                print("%s: %d" % (cube, an))
                
           
            if cube in active_cubes3d and an not in [2,3]:
                if cube not in cubes_to_remove:
                    cubes_to_remove.append(cube)
            elif cube not in active_cubes3d and an == 3:
                if cube not in cubes_to_add:
                    cubes_to_add.append(cube)
            # print(cube)

        for cube in cubes_to_add:
            active_cubes3d.append(cube)
        for cube in cubes_to_remove:
            active_cubes3d.remove(cube)
        
        # print(cubes_to_add)
        # print(cubes_to_remove)


        # print("add: %s" % cubes_to_add)
        # print("remove: %s" % cubes_to_remove)
        # print("active: %s" % active_cubes)

    print("There are %d active cubes" % len(active_cubes3d))
    # print("!!!")
    # print(min(next_grid))
    # print(min(next_grid)[0])
    # mn = min(next_grid)
    # mx = max(next_grid)
    # for z in range(mn[2], mx[2]+ 1):
    #     print("\n")
    #     for x in range(mn[0], mx[0]+ 1):
    #         ln = ''
    #         for y in range(mn[1], mx[1]+ 1):
    #             if [x,y,z] in active_cubes3d:
    #                 ln = ln + "#"
    #             else:
    #                 ln = ln + '.'
    #         print(ln)
    
def part2(n):
    start_grid = copy.deepcopy(grid4d)
    for i in range(0, n):
        next_grid = []
        for cube in start_grid:
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    for z in range(-1,2,1):
                        for w in range(-1,2,1):
                            if not [cube[0] + x, cube[1] + y, cube[2] + z, cube[3] + w] in next_grid:
                                next_cube = [cube[0] + x, cube[1] + y, cube[2] + z, cube[3] + w]
                                next_grid.append(next_cube)
                                if 
        start_grid = copy.deepcopy(next_grid)
        cubes_to_add = []
        cubes_to_remove = []
       
        for cube in next_grid:
            neighbors = []
            # print(cube)
            an = 0
            for ac in active_cubes4d:
                if ac == cube:
                    pass
                elif abs(ac[0] - cube[0]) < 2 and abs(ac[1] - cube[1]) < 2 and abs(ac[2] - cube[2]) < 2 and abs(ac[3] - cube[3]) < 2:
                    an += 1
                
           
            if cube in active_cubes4d and an not in [2,3]:
                if cube not in cubes_to_remove:
                    cubes_to_remove.append(cube)
            elif cube not in active_cubes4d and an == 3:
                if cube not in cubes_to_add:
                    cubes_to_add.append(cube)
            # print(cube)

        for cube in cubes_to_add:
            active_cubes4d.append(cube)
        for cube in cubes_to_remove:
            active_cubes4d.remove(cube)

        # print("add: %s" % cubes_to_add)
        # print("remove: %s" % cubes_to_remove)
        # print("active: %s" % active_cubes)
    print("There are %d active cubes" % len(active_cubes4d))
                

# part1(2)
part2(6)