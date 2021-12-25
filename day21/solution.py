from utils.file import read_file_content


CACHE = {}


def throw_dice(p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    if (p1, p2, s1, s2) in CACHE:
        return CACHE[(p1, p2, s1, s2)]

    result = (0, 0)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                move = ((p1 + d1 + d2 + d3 - 1) % 10) + 1
                score = s1 + move
                (w2, w1) = throw_dice(p2, move, s2, score)
                result = (result[0]+w1, result[1]+w2)
    CACHE[(p1, p2, s1, s2)] = result
    return result


def solve_part1(inp: str) -> int:
    players = inp.split("\n")
    positions = [int(players[0].split(" ")[-1]), int(players[1].split(" ")[-1])]
    scores = [0, 0]
    turns = 0
    while True:
        player = turns % 2
        start_val = turns*3 % 100
        dice = 0
        for i in range(0, 3):
            dice += ((start_val+i) % 100) + 1

        positions[player] = ((positions[player]+dice-1) % 10) + 1
        scores[player] += positions[player]
        turns += 1
        if scores[player] >= 1000:
            break

    losing_score = scores[turns % 2]
    throws = turns*3

    return losing_score * throws


def solve_part2(inp: str) -> int:
    players = inp.split("\n")
    p1 = int(players[0].split(" ")[-1])
    p2 = int(players[1].split(" ")[-1])
    s1 = s2 = 0
    return max(throw_dice(p1, p2, s1, s2))


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