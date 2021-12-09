def read_file_content(path: str) -> str:
    file = open(path, "r")
    r = file.read()
    file.close()

    return r


def get_neighbours(grid, x, y):
    result = set()
    if x > 0:
        result.add((x-1, y))
    if y > 0:
        result.add((x, y-1))
    if x < len(grid[0])-1:
        result.add((x+1, y))
    if y < len(grid)-1:
        result.add((x, y+1))
    return result


def solve_part1(input: str) -> int:
    lines = input.split("\n")

    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    result = 0
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            n = get_neighbours(grid, x, y)
            r = True
            for c in n:
                if grid[c[1]][c[0]] <= grid[y][x]:
                    r = False
            if r:
                result += grid[y][x]+1

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    unvisited = set([(x, y) for x in range(len(lines[0])) for y in range(len(lines)) if grid[y][x] != 9])
    toVisit = {unvisited.pop()}

    basins = []
    cur_basin = 0
    while len(toVisit) > 0:
        cur_point = toVisit.pop()
        n = get_neighbours(grid, cur_point[0], cur_point[1])

        cur_basin += 1

        for key in n:
            if key not in toVisit and key in unvisited:
                toVisit.add(key)
                unvisited.remove(key)

        if len(toVisit) == 0:
            basins.append(cur_basin)
            cur_basin = 0
            if len(unvisited) > 0:
                toVisit.add(unvisited.pop())

    sorted_basins = sorted(basins)[-3:]
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]


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