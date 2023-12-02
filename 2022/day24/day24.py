import os
from aocd import lines, submit, get_data
from collections import deque

from collections import deque
import math


MapStrings = []
for line in lines:
    MapStrings.append(line)

WallSet = set()
RightBlizz = set()
LeftBlizz = set()
UpBlizz = set()
DownBlizz = set()


for y, n in enumerate(MapStrings):
    for x, c in enumerate(n):
        Loc = (x, y)
        if c == ".":
            if y == 0:
                StartPoint = Loc
            else:
                EndPoint = Loc
        elif c == ">":
            RightBlizz.add(Loc)
        elif c == "<":
            LeftBlizz.add(Loc)
        elif c == "^":
            UpBlizz.add(Loc)
        elif c == "v":
            DownBlizz.add(Loc)
        elif c == "#":
            WallSet.add(Loc)
SX, SY = StartPoint
WallSet.add((SX, SY - 1))
SX, SY = EndPoint
WallSet.add((SX, SY + 1))

Width = len(MapStrings[0]) - 2
Height = len(MapStrings) - 2
LCM = math.lcm(Width, Height)


Starts = [StartPoint, EndPoint, StartPoint]
Ends = [EndPoint, StartPoint, EndPoint]
Directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]
PrevMinute = 0
for v in range(3):
    StartPoint = Starts[v]
    EndPoint = Ends[v]
    ImperialFrontier = deque()
    ImperialCore = set()
    ImperialFrontier.append((PrevMinute, StartPoint))
    CurrentBlizzards = set()
    LastMinute = PrevMinute
    while ImperialFrontier:
        CurrentMinute, Location = ImperialFrontier.popleft()
        NewMinute = CurrentMinute + 1
        if Location == EndPoint:
            if v == 0:
                Part1Answer = CurrentMinute
            if v == 2:
                Part2Answer = CurrentMinute
            PrevMinute = CurrentMinute
            break

        if NewMinute > LastMinute:
            print(NewMinute, len(ImperialFrontier))
            LastMinute = NewMinute
            CurrentBlizzards.clear()
            for X, Y in UpBlizz:
                NY = ((Y - NewMinute - 1) % Height) + 1
                CurrentBlizzards.add((X, NY))
            for X, Y in DownBlizz:
                NY = ((Y + NewMinute - 1) % Height) + 1
                CurrentBlizzards.add((X, NY))
            for X, Y in RightBlizz:
                NX = ((X + NewMinute - 1) % Width) + 1
                CurrentBlizzards.add((NX, Y))
            for X, Y in LeftBlizz:
                NX = ((X - NewMinute - 1) % Width) + 1
                CurrentBlizzards.add((NX, Y))

        X, Y = Location
        for DX, DY in Directions:
            NX, NY = X + DX, Y + DY
            NewLoc = (NX, NY)
            MinModulo = NewMinute % LCM
            NewCheckTuple = (MinModulo, NewLoc)
            if (
                NewLoc not in WallSet
                and NewLoc not in CurrentBlizzards
                and NewCheckTuple not in ImperialCore
            ):
                ImperialFrontier.append((NewMinute, NewLoc))
                ImperialCore.add(NewCheckTuple)


print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
