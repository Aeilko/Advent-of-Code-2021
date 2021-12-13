from utils.file import read_file_content


def fold (fold, grid):
    tmp = fold.split("=")
    direction = tmp[0][-1]
    val = int(tmp[1])

    toRemove = set()
    toAdd = set()
    for (x, y) in grid:
        if direction == 'x':
            if x > val:
                toAdd.add((val-(x-val), y))
                toRemove.add((x, y))
        if direction == 'y':
            if y > val:
                toAdd.add((x, val-(y-val)))
                toRemove.add((x, y))

    grid = (grid-toRemove) | toAdd

    return grid


def solve_part1(input: str) -> int:
    (points, folds) = input.split("\n\n")
    grid = set()

    for point in points.split("\n"):
        (x, y) = [int(x) for x in point.split(",")]
        grid.add((x, y))

    folds = folds.split("\n")
    grid = fold(folds[0], grid)

    return len(grid)


def solve_part2(input: str) -> int:
    (points, folds) = input.split("\n\n")
    grid = set()

    for point in points.split("\n"):
        (x, y) = [int(x) for x in point.split(",")]
        grid.add((x, y))

    folds = folds.split("\n")
    for f in folds:
        grid = fold(f, grid)

    maxX = 0
    maxY = 0
    for (x, y) in grid:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

    for y in range(maxY+1):
        line = ""
        for x in range(maxX+1):
            if (x,y) in grid:
                line += "##"
            else:
                line += "  "
        print(line)
        print(line)

    return -1


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