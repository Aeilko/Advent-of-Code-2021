from utils.file import read_file_content


def calc_score(board, nums):
    score = 0

    for row in board:
        for val in row:
            score += val

    cols = [5]*5
    rows = [5]*5

    for i in range(len(nums)):
        num = nums[i]
        for y in range(5):
            for x in range(5):
                if board[y][x] == num:
                    score -= num
                    rows[y] -= 1
                    cols[x] -= 1
                    if rows[y] == 0 or cols[x] == 0:
                        return i, score*num
    return None, None


def solve_part1(input: str) -> int:
    lines = input.split("\n")

    nums = [int(x) for x in lines[0].split(",")]
    boards = []
    board = []
    for i in range(2, len(lines)):
        line = lines[i]
        if line == "":
            boards.append(board)
            board = []
        else:
            row = [int(x) for x in line.split(" ") if x != ""]
            board.append(row)

    minRound = len(nums)
    minScore = 0
    for board in boards:
        (round, score) = calc_score(board, nums)
        if round != None and round < minRound:
            minRound = round
            minScore = score

    return minScore


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    nums = [int(x) for x in lines[0].split(",")]
    boards = []
    board = []
    for i in range(2, len(lines)):
        line = lines[i]
        if line == "":
            boards.append(board)
            board = []
        else:
            row = [int(x) for x in line.split(" ") if x != ""]
            board.append(row)

    maxRound = 0
    maxScore = 0
    for board in boards:
        (round, score) = calc_score(board, nums)
        if round != None and round > maxRound:
            maxRound = round
            maxScore = score

    return maxScore


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