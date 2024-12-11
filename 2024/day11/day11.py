from aocd import lines, submit, get_data
from functools import cache


test_data = ["125 17"]


def blink(a):
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    The left half of the digits are engraved on the new left stone,
    and the right half of the digits are engraved on the new right stone.
    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

    If none of the other rules apply, the stone is replaced by a new stone;
    the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    new_list = []
    for num in a:
        if num == 0:
            new_list.append(1)
        elif len(str(num)) % 2 == 0:
            h = int(len(str(num)) / 2)
            left_num = int(str(num)[0:h])
            right_num = int(str(num)[h:])
            new_list.append(left_num)
            new_list.append(right_num)
        else:
            new_list.append(2024 * num)

    return new_list


def part1():
    # data = test_data[0]
    data = lines[0]

    a = [int(x) for x in data.split(" ")]
    for _ in range(0, 25):
        a = blink(a)
    print(len(a))

    ans1 = len(a)
    return ans1


def part2():
    # data = test_data[0]
    data = lines[0]
    a = tuple(data.split())

    @cache
    def StoneShift(NumberStr):
        if NumberStr == "0":
            return "1", None
        Leng = len(NumberStr)
        if Leng % 2 == 0:
            Front, Back = NumberStr[: Leng // 2], NumberStr[Leng // 2 :]
            Back = str(int(Back))
            return Front, Back
        else:
            NumInt = int(NumberStr)
            return str(NumInt * 2024), None

    StartDict = {}
    for t in a:
        if t in StartDict:
            StartDict[t] += 1
        else:
            StartDict[t] = 1

    for _ in range(75):
        NextDict = {}
        for n in StartDict:
            Quantity = StartDict[n]
            A, B = StoneShift(n)
            for o in [A, B]:
                if o is None:
                    continue
                if o in NextDict:
                    NextDict[o] += Quantity
                else:
                    NextDict[o] = Quantity
        StartDict = NextDict.copy()

    ans2 = sum(StartDict.values())
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=11, year=2024)
submit(ans2, part="b", day=11, year=2024)
