import copy

from utils.file import read_file_content


def parse_input(inp):
    lines = inp.split("\n")
    grid = [[]]*len(lines)
    for i in range(len(lines)):
        row = []
        for c in lines[i]:
            row.append(c)
        grid[i] = row
    return grid


def perform_step(grid):
    moves = 0
    for y in range(len(grid)):
        first_occupied = False
        prev_moved = False
        for x in range(len(grid[0])):
            if x == 0 and grid[y][x] != '.':
                first_occupied = True
            if prev_moved:
                prev_moved = False
                continue
            if grid[y][x] == '>':
                if x == len(grid[0])-1:
                    if not first_occupied:
                        grid[y][0] = '>'
                        grid[y][x] = '.'
                        prev_moved = True
                        moves += 1
                elif grid[y][x+1] == '.':
                    grid[y][x] = '.'
                    grid[y][x+1] = '>'
                    prev_moved = True
                    moves += 1
    for x in range(len(grid[0])):
        first_occupied = False
        prev_moved = False
        for y in range(len(grid)):
            if y == 0 and grid[y][x] != '.':
                first_occupied = True
            if prev_moved:
                prev_moved = False
                continue
            if grid[y][x] == 'v':
                if y == len(grid)-1:
                    if not first_occupied:
                        grid[0][x] = 'v'
                        grid[y][x] = '.'
                        prev_moved = True
                        moves += 1
                elif grid[y+1][x] == '.':
                    grid[y][x] = '.'
                    grid[y+1][x] = 'v'
                    prev_moved = True
                    moves += 1
    return grid, moves


def solve_part1(inp: str) -> int:
    grid = parse_input(inp)
    steps = 0
    while True:
        grid, moves = perform_step(grid)
        steps += 1
        # for g in grid:
        #     print(g)
        # break
        if moves == 0:
            break
    return steps


def test_part1():
    i = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(i)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    i = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(i)))
