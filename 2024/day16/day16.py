from aocd import lines, submit, get_data


from heapq import heappop, heappush


START = "S"
END = "E"
DIRECTIONS = {(0, 1), (-1, 0), (0, -1), (1, 0)}
WALL = "#"


def parse():
    return {(i, j): char for i, row in enumerate(lines) for j, char in enumerate(row)}


def find_in_maze(maze, point):
    return next(pos for pos, char in maze.items() if char == point)


def dijkstra(maze, start):
    queue = [(0, start, (0, 1), set())]  # score, position, direction, visited tiles
    seen_states = {
        pos: {
            direction: {"score": float("inf"), "tiles": set()}
            for direction in DIRECTIONS
        }
        for pos in maze.keys()
    }
    while queue:
        score, (row, col), (dr, dc), tiles = heappop(queue)
        allowed = DIRECTIONS - {(-dr, -dc)}  # avoid reversing direction
        for new_dr, new_dc in allowed:
            new_row, new_col = row + new_dr, col + new_dc
            if (new_row, new_col) not in maze or maze[new_row, new_col] == WALL:
                continue
            new_score = score + 1 + (1000 if (new_dr, new_dc) != (dr, dc) else 0)
            state = seen_states[new_row, new_col][new_dr, new_dc]
            if new_score > state["score"]:
                continue
            new_tiles = tiles | {(new_row, new_col)}
            state["score"] = new_score
            if new_score < state["score"]:
                state["tiles"] = new_tiles
            elif new_score == state["score"]:
                state["tiles"] |= new_tiles
            heappush(
                queue, (new_score, (new_row, new_col), (new_dr, new_dc), state["tiles"])
            )
    return seen_states


def solve(seen_states, end):
    min_direction = min(seen_states[end].values(), key=lambda d: d["score"])
    return min_direction["score"], len(min_direction["tiles"]) + 1


def part1():
    maze = parse()
    start = find_in_maze(maze, START)
    end = find_in_maze(maze, END)
    maze[start] = "."
    maze[end] = "."
    seen_states = dijkstra(maze, start)
    print(solve(seen_states, end))


part1()


# uncomment these lines to submit
# submit(ans1, part="a", day=16, year=2024)
# submit(ans2, part="b", day=16, year=2024)
