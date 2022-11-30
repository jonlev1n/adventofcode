import copy
import time
import re
import math
file = open("/Users/jonathanlevin/git/adventofcode2020/day14/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day14/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day14/test_input2.txt", "r")


def part1():
    lines = file.readlines()
    mask = ''
    mem = {}
    for line in lines:
        if "mask" in line:
            mask = line.split('= ')[1].replace("\n", '')
        else:
            addr = re.search('\\[([0-9]*?)\\]', line).group(1)
            value = int(line.split('= ')[1])
            # print("address: %d" % int(addr))
            # convert the value to binary 
            # print(mask)
            bin_val = bin(value)[2:]
            # add 36 - len(mask) zeros
            header = ''.join('0' for i in range(0, 36 - len(bin_val)))
            value = header + bin_val

            # print("before: %s" % value)
            masked_value = ''
            for i in range(0, len(mask)):
                if mask[i] == 'X':
                    masked_value = masked_value + ''.join(value[i])
                else:
                    masked_value = masked_value + ''.join(mask[i]) 

            # print("after:  %s" % masked_value)
            # the evaluate the value of the address
            dec_value = 0
            for i in range(0, len(masked_value)):
                dec_value += int(masked_value[i]) * 2**(len(masked_value) - i - 1)
            mem[addr] = dec_value

    return sum(mem.values())


# p1 = part1()
# print(p1)


def part2():
    lines = file.readlines()
    mask = ''
    mem = {}
    for line in lines:
        if "mask" in line:
            mask = line.split('= ')[1].replace("\n", '')
        else:
            addr = re.search('\\[([0-9]*?)\\]', line).group(1)
            addr_value = int(line.split('= ')[1])
            # print("address: %d" % int(addr))
            # print("addr value: %d" % addr_value)
            # print("mask: %s" % mask)
            # convert the value to binary
            # print(mask)
            bin_addr = bin(int(addr))[2:]
            # print("bin_addr: %s" % bin_addr)
            # add 36 - len(mask) zeros
            header = ''.join('0' for i in range(0, 36 - len(bin_addr)))
            value = header + bin_addr

            # print("before: %s" % value)
            masked_value = ''
            for i in range(0, len(mask)):
                if mask[i] == 'X':
                    masked_value = masked_value + ''.join('X')
                elif mask[i] == '0':
                    masked_value = masked_value + ''.join(value[i])
                else:
                    masked_value = masked_value + ''.join('1')
            # print("after: %s" % masked_value)
            
            address_list = [] 
            total_addresses = 2**(masked_value.count('X'))
            # print("total_address: %d" % total_addresses)
            

            for i in range(0, total_addresses):
                bin_replacement = bin(i)[2:]
                # if bin_replacement is not long enough, pad with zeros
                padding = ''
                if len(bin_replacement) < math.log(total_addresses, 2):
                    padding = ''.join('0' for i in range(0, int(math.log(total_addresses, 2)) - len(bin_replacement)))
                bin_replacement = padding + bin_replacement
                x_count = 0
                possible_addr = ''
                dec_value = 0
                for j in range(0, len(masked_value)):
                    if masked_value[j] == 'X':
                        possible_addr = possible_addr + ''.join(bin_replacement[x_count])
                        x_count += 1
                    else:
                        possible_addr = possible_addr + ''.join(masked_value[j])
                    dec_value += int(possible_addr[j]) * 2**(len(masked_value) - j - 1)
                
                address_list.append(dec_value)
            # print("address list: %s" % address_list)
            for addr in address_list:
                mem[addr] = addr_value
    return sum(mem.values())

p2 = part2()
# print(p2)
