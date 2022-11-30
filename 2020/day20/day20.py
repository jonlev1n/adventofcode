import copy
import time
import re
import math
import numpy as np

# file = open("/Users/jon/git/adventofcode2020/day20/test_input.txt", "r")
file = open("/Users/jon/git/adventofcode2020/day20/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day20/test_input2.txt", "r")

lines = file.read().splitlines()

tiles = {}
tile = []
for line in lines:
    if "Tile" in line:
        key = line.split(" ")[1]
        key = key.replace(":", "")
    else:
        if line == "":
            # print(tile)
            tiles[key] = np.array(tile)
            tile = []
        else:
            tile.append([char for char in line])


def get_borders(bid):
    t = tiles[bid]
    t_border = t[0]
    b_border = t[len(t) - 1]
    l_border = np.array([p[0] for p in t])
    r_border = np.array([p[len(p) - 1] for p in t])
    return [t_border, r_border, b_border, l_border]
    # print(borders)
    # we want corner tiles which will only have 2 border that appear in different tiles
    # the tiles coule be rotated, so the borders could match forward or back


corners = {}
adjacent_tiles = {}
# tile_pool = [tile_id for tile_id in tiles]
for id1 in tiles:
    corner_count = 0
    adj_t = []
    # print("Comparing to: %s" % id1)
    for id2 in tiles:
        if id1 == id2:
            pass
        else:
            borders_1 = get_borders(id1)
            borders_2 = get_borders(id2)
            for idx1, b1 in enumerate(borders_1):
                for idx2, b2 in enumerate(borders_2):
                    # if id2 not in tile_pool:
                    #     break
                    condition1 = b1 == b2
                    condition2 = b1 == np.flip(b2)
                    if condition1.all() or condition2.all():
                        corner_count += 1
                        adj_t.append(id2)

    # print(condition)
    # # print(intersect)
    # if condition:
    #     corner_count += 1
    #     adj_t.append(border2)
    adjacent_tiles[id1] = adj_t
    corners[id1] = corner_count

r = [c for c in corners if corners[c] == 2]
print(r)
start_tile = "1123"  # for real input
# start_tile = "1951"  # for test input
size = int(math.sqrt(len(tiles)))
image = [[0 for i in range(0, size)] for i in range(0, size)]
tiles[start_tile] = np.flip(tiles[start_tile], 1)  # for real input
# tiles[start_tile] = np.flip(tiles[start_tile], 0)  # for test input

image[0][0] = start_tile
# print(image)
# start with a corner tile
tile_map = [start_tile]
for id1 in tile_map:
    x_idx = np.argwhere(np.array(image) == id1)[0][0]
    y_idx = np.argwhere(np.array(image) == id1)[0][1]
    # print(x_idx)
    # print(y_idx)
    for id2 in adjacent_tiles[id1]:
        if id2 in tile_map:
            pass
        else:
            # print("modifying tile %s" % id2)
            borders_1 = get_borders(id1)
            borders_2 = get_borders(id2)
            for idx1, b1 in enumerate(borders_1):
                for idx2, b2 in enumerate(borders_2):
                    condition1 = b1 == b2
                    condition2 = b1 == np.flip(b2)
                    if condition1.all() or condition2.all():
                        rotations = 0
                        flip_dir = 1 if idx1 in [0, 2] else 0
                        # next one goes below
                        if idx1 in [0, 2]:
                            image[x_idx + 1][y_idx] = id2
                        else:
                            image[x_idx][y_idx + 1] = id2
                        if abs(idx1 - idx2) < 2:
                            rotations = (2 - (idx1 - idx2)) % 4
                            tiles[id2] = copy.deepcopy(
                                np.rot90(tiles[id2], k=rotations)
                            )
                            new_b1 = get_borders(id1)
                            new_b2 = get_borders(id2)
                            new_idx2 = (
                                4 + idx2 - rotations
                                if (idx2 - rotations) < 0
                                else (idx2 - rotations)
                            )
                            if (new_b1[idx1] == np.flip(new_b2[new_idx2])).all():
                                tiles[id2] = copy.deepcopy(
                                    np.flip(tiles[id2], flip_dir)
                                )

                        else:
                            if condition2.all():
                                # print("0 rotations but backwards!")
                                tiles[id2] = copy.deepcopy(
                                    np.flip(tiles[id2], flip_dir)
                                )

            tile_map.append(id2)


def part1():

    edge_val = 1
    for c in corners:
        if corners[c] == 2:
            edge_val *= int(c)
    print(edge_val)

    # tile_map = [[0 for i in range(0,size)] for i in range(0,size)]
    # print(tile_map)


# part1()


def part2():
    trimmed_tiles = {}
    for tile in tiles:
        trimmed = tiles[tile][1:9, 1:9]
        trimmed_tiles[tile] = trimmed
        # print("tile: %s" % tile)
        # print(tiles[tile])
        # print("")
        # print(trimmed)

    total_rows = []
    for row in image:
        # tu = (trimmed_tiles[arr] for arr in row)
        # print(tu)
        total_row = np.hstack(trimmed_tiles[arr] for arr in row)
        total_rows.append(total_row)
        # print(total_row)

    img = np.vstack(t for t in total_rows)
    # print(img)
    # print("")
    # print(np.rot90(img))
    seamonster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
    seamonster = np.array([[y == "#" for y in x] for x in seamonster[:-1].split("\n")])
    # seamonster = np.array(np.vstack([seamonster[0], seamonster[1], seamonster[2]]))
    # print(seamonster)

    total_hash = 0
    for i in range(0, len(img)):
        for j in range(0, len(img)):
            if img[i, j] == "#":
                total_hash += 1
    # print(total_hash)
    s = 0
    o = [
        img,
        np.rot90(img, k=1),
        np.rot90(img, k=2),
        np.rot90(img, k=3),
        np.flip(img, 0),
        np.flip(img, 1),
        np.flip(np.rot90(img, k=1), 0),
        np.flip(np.rot90(img, k=1), 1),
    ]
    for img in o:
        for i in range(0, len(img) - 2):
            for j in range(0, len(img) - 19):
                chunk = img[i : i + 3, j : j + 20]
                chunk = np.array([[y == "#" for y in x] for x in chunk])
                # print(chunk)
                # print("")
                if np.all(chunk | ~seamonster):
                    # print(Grid(cut),'\n')
                    # print(Grid(cut & seamonster),'\n')
                    # img[i : i + 3, j : j + 20] &= ~seamonster
                    s += 1
    # print(s)
    seamonster_hash = 15
    print(total_hash - s * seamonster_hash)


part2()

# print(tiles["1951"])
# print("\n")
# print(np.flip(tiles["1951"], 0))
# print("\n")
# print(np.flip(tiles["1951"], 1))
# print("\n")

# for idx in tiles:
#     print("tile %s" % idx)
#     # print(np.rot90(tiles[idx],k=2))
#     # print(np.flip(tiles[idx], 1))
#     print(np.flip(tiles[idx], 0))
#     # print(tiles[idx])
#     print("\n")

