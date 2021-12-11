from utils.file import read_file_content


def get_neighbours(grid, x, y):
    result = set()
    if x > 0:
        if y > 0:
            result.add((x-1, y-1))
        result.add((x-1, y))
    if y > 0:
        if x < len(grid[0])-1:
            result.add((x+1, y-1))
        result.add((x, y - 1))
    if x < len(grid[0]) - 1:
        if y < len(grid)-1:
            result.add((x+1, y+1))
        result.add((x + 1, y))
    if y < len(grid) - 1:
        if x > 0:
            result.add((x-1, y+1))
        result.add((x, y + 1))
    return result


def step(grid):
    score = 0
    nineSet = set()
    setNul = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
            if grid[y][x] == 10:
                nineSet.add((x, y))

    while len(nineSet) > 0:
        (x, y) = nineSet.pop()
        setNul.add((x, y))
        score += 1
        n = get_neighbours(grid, x, y)
        for xx, yy in n:
            point = (xx, yy)
            if point not in nineSet and point not in setNul:
                grid[yy][xx] += 1
                if grid[yy][xx] == 10:
                    nineSet.add((xx, yy))

    for x, y in setNul:
        grid[y][x] = 0

    return grid, score


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    grid = []
    for line in lines:
        grid.append([int(x) for x in line])

    result = 0
    for i in range(100):
        grid, score = step(grid)
        result += score

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    grid = []
    for line in lines:
        grid.append([int(x) for x in line])

    total = len(grid[0])*len(grid)

    i = 0
    while True:
        i += 1
        grid, score = step(grid)
        if score == total:
            break

    return i


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