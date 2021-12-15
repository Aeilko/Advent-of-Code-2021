from utils.file import read_file_content


# TODO: Look into Priority Queues in Python, that should be way better then my current sorted list implementation
def sort_nodes(e):
    return e[1]


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


def find_path(grid):
    toVisit = []
    visited = set()
    toVisit.append(((0, 0), 0))
    TARGET = (len(grid[0]) - 1, len(grid) - 1)
    result = 0
    while len(toVisit) > 0:
        toVisit.sort(key=sort_nodes, reverse=True)
        ((x, y), cost) = toVisit.pop()
        if (x, y) == TARGET:
            result = cost
            break
        n = get_neighbours(grid, x, y)
        for node in n:
            if node not in visited:
                nc = cost + grid[node[1]][node[0]]
                tmp = [x[1] for x in toVisit if x[0] == node]
                if len(tmp) > 0:
                    if nc < tmp[0]:
                        toVisit.remove((node, tmp[0]))
                        toVisit.append((node, nc))
                else:
                    toVisit.append((node, nc))
        visited.add((x, y))

    return result


def solve_part1(input: str) -> int:
    lines = input.split("\n")

    grid = []
    for line in lines:
        row = [int(x) for x in line]
        grid.append(row)

    return find_path(grid)


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    grid = []
    for line in lines:
        row = []
        for i in range(5):
            row.extend([((int(x)+i-1) % 9)+1 for x in line])
        grid.append(row)

    rows = len(grid)
    for i in range(4):
        for j in range(rows):
            grid.append([((int(x)+i) % 9)+1 for x in grid[j]])

    return find_path(grid)


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