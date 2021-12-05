from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    chart = {}
    for line in lines:
        (start, end) = line.split(" -> ")
        (startX, startY) = [int(a) for a in start.split(",")]
        (endX, endY) = [int(a) for a in end.split(",")]

        if startX == endX:
            x = startX
            lowY = startY
            highY = endY
            if endY < startY:
                lowY = endY
                highY = startY
            for y in range(lowY, highY+1):
                if x in chart.keys():
                    if y in chart[x].keys():
                        chart[x][y] += 1
                    else:
                        chart[x][y] = 1
                else:
                    chart[x] = {}
                    chart[x][y] = 1
        elif startY == endY:
            y = startY
            lowX = startX
            highX = endX
            if endX < startX:
                lowX = endX
                highX = startX
            for x in range(lowX, highX+1):
                if x in chart.keys():
                    if y in chart[x].keys():
                        chart[x][y] += 1
                    else:
                        chart[x][y] = 1
                else:
                    chart[x] = {}
                    chart[x][y] = 1

    result = 0
    for i in chart.keys():
        for j in chart[i].keys():
            if chart[i][j] > 1:
                result += 1

    return result


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    chart = {}
    for line in lines:
        (start, end) = line.split(" -> ")
        (startX, startY) = [int(a) for a in start.split(",")]
        (endX, endY) = [int(a) for a in end.split(",")]

        if startX == endX:
            x = startX
            lowY = startY
            highY = endY
            if endY < startY:
                lowY = endY
                highY = startY
            for y in range(lowY, highY + 1):
                if x in chart.keys():
                    if y in chart[x].keys():
                        chart[x][y] += 1
                    else:
                        chart[x][y] = 1
                else:
                    chart[x] = {}
                    chart[x][y] = 1
        elif startY == endY:
            y = startY
            lowX = startX
            highX = endX
            if endX < startX:
                lowX = endX
                highX = startX
            for x in range(lowX, highX + 1):
                if x in chart.keys():
                    if y in chart[x].keys():
                        chart[x][y] += 1
                    else:
                        chart[x][y] = 1
                else:
                    chart[x] = {}
                    chart[x][y] = 1
        else:
            directionX = 1
            if startX > endX:
                directionX = -1
            directionY = 1
            if startY > endY:
                directionY = -1

            length = abs(startX-endX)
            for i in range(length+1):
                x = startX + (i*directionX)
                y = startY + (i*directionY)

                if x in chart.keys():
                    if y in chart[x].keys():
                        chart[x][y] += 1
                    else:
                        chart[x][y] = 1
                else:
                    chart[x] = {}
                    chart[x][y] = 1

    result = 0
    for i in chart.keys():
        for j in chart[i].keys():
            if chart[i][j] > 1:
                result += 1

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