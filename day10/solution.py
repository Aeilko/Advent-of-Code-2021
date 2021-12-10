import math
from collections import deque

from utils.file import read_file_content


OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
INVERSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
POINTS2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def solve_part1(input: str) -> int:
    lines = input.split("\n")

    result = 0
    for line in lines:
        stack = deque()
        for c in line:
            if c in OPEN:
                stack.append(c)
            elif c in CLOSE:
                c1 = stack.pop()
                if INVERSE[c1] != c:
                    result += POINTS[c]

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    results = []
    for line in lines:
        stack = deque()
        inc = False
        for c in line:
            if c in OPEN:
                stack.append(c)
            elif c in CLOSE:
                c1 = stack.pop()
                if INVERSE[c1] != c:
                    inc = True
                    break
        if not inc and len(stack) > 0:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                score *= 5
                score += POINTS2[INVERSE[c]]
            results.append(score)

    r = sorted(results)
    return r[math.floor(len(r)/2)]


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