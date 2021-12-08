from utils.file import read_file_content


numbers = {}
numbers[0] = {'a', 'b', 'c', 'e', 'f', 'g'}
numbers[1] = {'c', 'f'}
numbers[2] = {'a', 'c', 'd', 'e', 'g'}
numbers[3] = {'a', 'c', 'd', 'f', 'g'}
numbers[4] = {'b', 'c', 'd', 'f'}
numbers[5] = {'a', 'b', 'd', 'f', 'g'}
numbers[6] = {'a', 'b', 'd', 'e', 'f', 'g'}
numbers[7] = {'a', 'c', 'f'}
numbers[8] = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
numbers[9] = {'a', 'b', 'c', 'd', 'f', 'g'}


def find_mapping(input):
    words = input.split(" ")
    all_chars = [c for c in "abcdefg"]
    nums = {}
    mapping = {}

    # Count occurrences
    occurences = {}
    for x in all_chars:
        occurences[x] = 0
    for word in words:
        for x in word:
            occurences[x] += 1

    for char in occurences:
        if occurences[char] == 4:
            mapping['e'] = char
        elif occurences[char] == 6:
            mapping['b'] = char
        elif occurences[char] == 9:
            mapping['f'] = char

    # Find 1
    for word in words:
        if len(word) == 2:
            chars = [c for c in word]
            nums[1] = set(chars)
            mapping['c'] = [c for c in word if c != mapping['f']][0]

    # Find 7
    for word in words:
        if len(word) == 3:
            nums[7] = set([c for c in word])
            tmp = nums[7]-nums[1]
            mapping['a'] = tmp.pop()
            break

    # Find 4
    for word in words:
        if len(word) == 4:
            nums[4] = set([c for c in word])
            tmp = nums[4] - nums[1] - set(mapping['b'])
            mapping['d'] = tmp.pop()

    # Find g
    ac = set([c for c in "abcdefg"])
    for x in mapping:
        ac.remove(mapping[x])
    mapping['g'] = ac.pop()

    reverse_mapping = {}
    for x in mapping:
        reverse_mapping[mapping[x]] = x

    return reverse_mapping


def solve_part1(input: str) -> int:
    lines = input.split("\n")

    result = 0
    for line in lines:
        (i, o) = line.split(" | ")
        words = o.split(" ")
        for word in words:
            if word == "|":
                continue

            if len(word) in [2, 3, 4, 7]:
                result += 1

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    result = 0
    for line in lines:
        (i, o) = line.split(" | ")
        mapping = find_mapping(i)

        words = o.split(" ")
        out = ""
        for word in words:
            lights = set()
            for c in word:
                lights.add(mapping[c])
            for x in numbers:
                if lights == numbers[x]:
                    out += str(x)
        # print(out)
        result += int(out)

    return result


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