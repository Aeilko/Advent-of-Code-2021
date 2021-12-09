from utils.file import read_file_content


def get_neighbours(grid, x, y):
    result = {}
    if x > 0:
        result[(x-1, y)] = grid[y][x-1]
    if y > 0:
        result[(x, y-1)] = grid[y-1][x]
    if x < len(grid[0])-1:
        result[(x+1, y)] = grid[y][x+1]
    if y < len(grid)-1:
        result[(x, y+1)] = grid[y+1][x]
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
                if n.get(c) <= grid[y][x]:
                    r = False
            if r:
                result += grid[y][x]+1

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    unvisited = [(x, y) for x in range(len(lines[0])) for y in range(len(lines)) if grid[y][x] != 9]
    toVisit = {unvisited[0]}

    basins = []
    curBasin = 0
    while len(toVisit) > 0:
        curPoint = toVisit.pop()
        x = curPoint[0]
        y = curPoint[1]
        n = get_neighbours(grid, x, y)

        curBasin += 1
        unvisited.remove(curPoint)

        for key in n:
            if key not in toVisit and key in unvisited:
                toVisit.add(key)

        if len(toVisit) == 0:
            basins.append(curBasin)
            curBasin = 0
            if len(unvisited) > 0:
                c = unvisited.pop()
                toVisit = {c}
                unvisited.append(c)

    n1 = max(basins)
    basins.remove(n1)
    n2 = max(basins)
    basins.remove(n2)
    n3 = max(basins)

    return n1*n2*n3


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