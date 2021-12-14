from utils.file import read_file_content


def parse_input(input):
    (element, rest) = input.split("\n\n")
    pairs = {}
    for i in range(len(element)-1):
        pair = element[i:i+2]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    rules = {}
    rest = rest.split("\n")
    for r in rest:
        (start, end) = r.split(" -> ")
        rules[start] = end

    return (pairs, rules)


def step(pairs, rules):
    new_pairs = {}
    for pair in pairs:
        if pair in rules:
            val = pairs[pair]
            c = rules[pair]
            p1 = pair[0] + c
            p2 = c + pair[1]
            for p in [p1, p2]:
                if p in new_pairs:
                    new_pairs[p] += val
                else:
                    new_pairs[p] = val
    return new_pairs


def scoring(pairs, input):
    occs = {}
    for pair in pairs:
        val = pairs[pair]
        for p in pair:
            if p in occs:
                occs[p] += val
            else:
                occs[p] = val

    min_val = 100000000000000000
    max_val = 0
    for c in occs:
        if c == input[0] or c == input[-1]:
            occs[c] += 1
        val = int(occs[c] / 2)
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

    return max_val - min_val


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    (pairs, rules) = parse_input(input)

    for i in range(10):
        pairs = step(pairs, rules)

    return scoring(pairs, lines[0])


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    (pairs, rules) = parse_input(input)

    for i in range(40):
        pairs = step(pairs, rules)

    return scoring(pairs, lines[0])


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