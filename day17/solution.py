from utils.file import read_file_content


def parse_input(input):
    (xvals, yvals) = input[15:].split(", y=")
    xstart, xend = [int(x) for x in xvals.split("..")]
    ystart, yend = [int(y) for y in yvals.split("..")]
    return xstart, xend, ystart, yend


def perform_step(sx, sy, dx, dy):
    rx = sx+dx
    ry = sy+dy
    dy -= 1
    if dx > 0:
        dx -= 1
    return rx, ry, dx, dy


def solve_part1(input: str) -> int:
    x_start, x_end, y_start, y_end = parse_input(input)

    max_y = 0
    for y in range(100, 0, -1):
        correct = False
        for x in range(x_end+1):
            passed = False
            dx = x
            dy = y
            cx = 0
            cy = 0
            y_vals = set()
            while cx <= x_end:
                cx, cy, dx, dy = perform_step(cx, cy, dx, dy)
                y_vals.add(cy)
                if cx > x_end or cy < y_start:
                    passed = True
                    break
                if x_start <= cx <= x_end and y_start <= cy <= y_end:
                    correct = True
                    y_max = max(y_vals)
                    if y_max > max_y:
                        max_y = y_max
                    break
            if correct:
                break
            if passed:
                continue
        if correct:
            break

    return max_y


def solve_part2(input: str) -> int:
    x_start, x_end, y_start, y_end = parse_input(input)

    initials = set()
    for y in range(y_start, 100):
        correct = False
        for x in range(x_end+1):
            passed = False
            dx = x
            dy = y
            cx = 0
            cy = 0
            while cx <= x_end:
                cx, cy, dx, dy = perform_step(cx, cy, dx, dy)
                if cx > x_end or cy < y_start:
                    passed = True
                    break
                if x_start <= cx <= x_end and y_start <= cy <= y_end:
                    # print((x, y))
                    initials.add((x, y))
                    break
            if passed:
                continue
        if correct:
            break

    return len(initials)


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