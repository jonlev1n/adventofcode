import copy
import time
file = open("/Users/jonathanlevin/git/adventofcode2020/day10/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day10/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day10/test_input2.txt", "r")
lines = file.readlines()

adapters = []
for line in lines:
    adapter = int(line)
    adapters.append(adapter)

low_buffer = 3
high_buffer = 3


def part1():
    jump_3 = 1
    jump_1 = 0
    initial_jump = min(adapters)
    if initial_jump == 3:
        jump_3 += 1
    elif initial_jump == 1:
        jump_1 += 1
        pass 
    adapters.sort()
    # print(adapters)
    for i in range(0, len(adapters) -1):
        if adapters[i+1] - adapters[i] == 1:
            jump_1 += 1
        elif adapters[i+1] - adapters[i] == 3:
            jump_3 += 1
        
    return jump_3 * jump_1




# p1 = part1()
# print(p1)

def part2():
    start_time = time.time()
    configurations = 1
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    # split_vals = []
    count = 0
    max_count = 0 
    for i in range(len(adapters) - 3):
        # for each number calculate # of possible next values...
        if(adapters[i+1] == max(adapters) or adapters[i+1] - adapters[i] >= 3 or adapters[i+2] - adapters[i] >=4):
            # the only choice is the next number... 
            n = 0
        elif adapters[i+1] - adapters[i] == 1 and adapters[i + 2] - adapters[i] == 2 and adapters[i+3] - adapters[i] == 3:
            n = 3
        else:
            n = 2

        
        
        if n != 0:
            count += 1

        if n == 2 or n == 0:
            max_count = count
            print("max count: %d" % max_count)
            if max_count == 3:
                configurations *= 7
            elif max_count == 2:
                configurations *= 4
            elif max_count == 1:
                configurations *= 2
            count = 0
    print("--------- %d ---------" % (time.time() - start_time))
    return configurations

            


p2 = part2()
print(p2)
