import copy

from utils.file import read_file_content


def run(inp, rounds):
    (iea, grid_inp) = inp.split("\n\n")
    grid_lines = grid_inp.split("\n")

    yl = len(grid_lines) + 2 * rounds
    xl = len(grid_lines[0]) + 2 * rounds

    # Create empty grid
    grid = [[]] * yl
    for i in range(yl):
        grid[i] = [False] * xl

    # Parse input grid
    for y in range(len(grid_lines)):
        for x in range(len(grid_lines[y])):
            if grid_lines[y][x] == '#':
                grid[y + rounds][x + rounds] = True

    for r in range(rounds):
        outer = False if iea[0] == '.' else r % 2 != 0
        grid = perform_step(grid, iea, outer)

    return score_grid(grid)


def perform_step(grid, iea, outside):
    result = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            val = get_val(grid, x, y, outside)
            result[y][x] = iea[val] == "#"
    return result


def get_val(grid, base_x, base_y, outers):
    r = ""
    for y in range(base_y-1, base_y+2):
        if y < 0 or y == len(grid):
            r += "111" if outers else "000"
        else:
            for x in range(base_x-1, base_x+2):
                if x < 0 or x == len(grid[y]):
                    r += "1" if outers else "0"
                else:
                    r += "1" if grid[y][x] else "0"
    return int(r, 2)


def score_grid(grid):
    score = 0
    for row in grid:
        for val in row:
            if val:
                score += 1
    return score


def display_grid(grid):
    for line in grid:
        r = ""
        for val in line:
            r += "#" if val else "."
        print(r)


def solve_part1(inp: str) -> int:
    return run(inp, 2)


def solve_part2(inp: str) -> int:
    return run(inp, 50)


def test_part1():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    input = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(input)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(input)))