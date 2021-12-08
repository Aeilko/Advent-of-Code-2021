from utils.file import read_file_content


def solve_part1(input: str) -> int:
    nums = [int(x) for x in input.split(",")]
    min = 100000000000000
    max = 0
    for x in nums:
        if x < min:
            min = x
        if x > max:
            max = x

    minVal = 100000000000000
    for i in range(min, max):
        score = 0
        for x in nums:
            score += abs(x-i)
        if score < minVal:
            minVal = score

    return minVal


def solve_part2(input: str) -> int:
    nums = [int(x) for x in input.split(",")]
    min = 1000000000000000000
    max = 0
    for x in nums:
        if x < min:
            min = x
        if x > max:
            max = x

    minVal = 1000000000000000000
    for i in range(min, max):
        score = 0
        for x in nums:
            tmp = abs(x-i)
            score += tmp * (tmp + 1) / 2
        if score < minVal:
            minVal = int(score)

    return minVal


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