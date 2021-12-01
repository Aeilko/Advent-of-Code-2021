from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    prev = int(lines[0])
    r = 0
    for x in range(1, len(lines)):
        if int(lines[x]) > prev:
            r += 1
        prev = int(lines[x])

    return r


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    prevsum = int(lines[0]) + int(lines[1]) + int(lines[2])
    r = 0
    for x in range(3, len(lines)):
        sum = int(lines[x-2]) + int(lines[x-1]) + int(lines[x])
        if sum > prevsum:
            r += 1
        prevsum = sum

    return r


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
