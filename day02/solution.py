from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    depth = 0
    forward = 0
    for l in lines:
        (move, d) = l.split(" ")
        d = int(d)
        if move == "forward":
            forward += d
        elif move == "down":
            depth += d
        elif move == "up":
            depth -= d
    return depth*forward


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    aim = 0
    depth = 0
    horizontal = 0
    for l in lines:
        (move, d) = l.split(" ")
        d = int(d)
        if move == "forward":
            horizontal += d
            depth += aim*d
        elif move == "down":
            aim += d
        elif move == "up":
            aim -= d
    return depth * horizontal


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
