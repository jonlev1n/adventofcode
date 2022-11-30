from aocd import lines


bitmap = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111",
}


test_data = "38006F45291200"
data = test_data


def convert_to_binary(s):
    return ''.join([bitmap[c] for c in s])

def num_from_binary(s):
    n = 0
    for idx, val in enumerate(reversed(s)):
        n += int(val) * 2 ** idx
    return n

def find_subpackets(b, subpackets=[]):

    if len(b) < 11:
        return subpackets
    v = num_from_binary(b[0:3])
    t = num_from_binary(b[3:6])
    
    if t == 4:
        for i in range(6, len(b), 5):
            if b[i] == "0":
                # end of packet
                subpackets.append(b[0:i+5])
                return find_subpackets(b[i+5:], subpackets)

    
    else:
        # is an operator
        i = b[6]
        if i == "0":
            # next 15 tell length of packets
            pl = num_from_binary(b[7:22])
            return(find_subpackets(b[22:22+pl]))
        if i == "1"







# def traverse_subpacket = 




# def get_literal(s):


def part1():
    b = convert_to_binary(data)
    # find_subpackets(b)
    s = find_subpackets("110100010100101001000100100")
    print(s)


part1()