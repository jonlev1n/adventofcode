import copy
file = open("/Users/jonathanlevin/git/adventofcode2020/day9/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day9/test_input.txt", "r")
lines = file.readlines()

numbers = []
for line in lines:
    number = int(line)
    numbers.append(number)

# preamble_length = 5
preamble_length = 25

def part1():
    for i in range(preamble_length, len(numbers)):
        num = numbers[i]
        preamble = []
        for j in range(i - preamble_length, i):
            preamble.append(numbers[j])

        if num > max(preamble) * 2 - 1:
            return num
        else:
            any_matches = False
            for p1 in preamble:
                for p2 in preamble:
                    if p1 == p2:
                        break
                    else:
                        if p1 + p2 == num:
                            any_matches = True
                            break
                        
            if any_matches == False:
                print("Found the offender:")
                return num
            

part1 = part1()
print(part1)
print("\n")

def part2():
    goal = part1
    # need to find a contiguous set 

    all_cont = []
    for i in range(0, len(numbers) - 1):
        cont = []
        for j in range(i, len(numbers) - 1):
            # if
            try:
                cont.append(numbers[j])
                if len(cont) >= 2:
                    all_cont.append(copy.deepcopy(cont))
            except:
                pass

    # now we have a list of all contiguous sets...
    # see which one sums to the specified number
    for cont in all_cont:
        if sum(cont) == goal:
            # return min + max
            return min(cont) + max(cont)

part2 = part2()
print(part2)