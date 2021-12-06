from utils.file import read_file_content


def solve_part1(input: str) -> int:
    fishes = [int(f) for f in input.split(",")]
    ages = [0]*9

    for f in fishes:
        ages[f] += 1

    for day in range(80):
        newFish = ages[0]
        for i in range(1, 9):
            ages[i-1] = ages[i]
        ages[8] = newFish
        ages[6] += newFish

    return sum(ages)


def solve_part2(input: str) -> int:
    fishes = [int(f) for f in input.split(",")]
    ages = [0]*9

    for f in fishes:
        ages[f] += 1

    for day in range(256):
        newFish = ages[0]
        for i in range(1, 9):
            ages[i - 1] = ages[i]
        ages[8] = newFish
        ages[6] += newFish

    return sum(ages)


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