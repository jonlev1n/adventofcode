import copy

file = open("/Users/jonathanlevin/git/adventofcode2020/day8/data.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day8/test_data.txt", "r")

lines = file.readlines()
operations = []
arguments = []
combined_ops = []

for line in lines:
    operation = line.split(" ")[0]
    argument = line.split(" ")[1]
    if argument[0] == "+":
        argument = int(argument[1:])
    elif argument[0] == '-':
        argument =  -1 * int(argument[1:])
    operations.append(operation)
    arguments.append(argument)
    combined_ops.append([operation, argument])



def find_loop():
    idx = 0
    accumulator = 0
    past_idxs = []
    while idx not in past_idxs:
        past_idxs.append(idx)

        # rules
        # if acc, add to accumulator execute next rule
        if combined_ops[idx][0] == 'acc':
            # accumulator code
            accumulator += combined_ops[idx][1]
            # advance idx
            idx += 1
        # if jmp, the idx jumps relative to itself
        elif combined_ops[idx][0] == 'jmp':
            idx += combined_ops[idx][1]
        # if nop do nothing, execute next rule
        elif combined_ops[idx][0] == 'nop':
            idx += 1

    return accumulator


def terminate():
    # global idx
    # global accumulator
    flipped_idxs = [] 
    for i in range(0, len(combined_ops)):
        accumulator = 0
        idx = 0
        past_idxs = []
        combined_ops_copy = copy.deepcopy(combined_ops)
        if combined_ops[i][0] == "jmp" and i not in flipped_idxs:
            combined_ops_copy[i][0] = "nop"
            flipped_idxs.append(i)
        elif combined_ops[i][0] == "nop" and i not in flipped_idxs:
            combined_ops_copy[i][0] = "jmp"
            flipped_idxs.append(i)

        while idx not in past_idxs:
            past_idxs.append(idx)
            try:
                test = combined_ops[idx][0]
            except:
                print('!!!')
                return accumulator
            # if acc, add to accumulator execute next rule
            if combined_ops_copy[idx][0] == 'acc':
                # accumulator code
                accumulator += combined_ops_copy[idx][1]
                # advance idx
                idx += 1
            # if jmp, the idx jumps relative to itself
            elif combined_ops_copy[idx][0] == 'jmp':
                idx += combined_ops_copy[idx][1]
            # if nop do nothing, execute next rule
            elif combined_ops_copy[idx][0] == 'nop':
                idx += 1

    return accumulator


    

# p = find_loop()
# print(p)

t = terminate()
print(t)


