from utils.file import read_file_content


def parse_instruction(line, grid):
    (mode, coords) = line.split(" ")
    (xcoords, ycoords, zcoords) = coords.split(",")
    (x_start, x_end) = [int(x) for x in xcoords[2:].split("..")]
    (y_start, y_end) = [int(y) for y in ycoords[2:].split("..")]
    (z_start, z_end) = [int(z) for z in zcoords[2:].split("..")]
    if x_start > 50 or x_start < -50:
        return grid

    if mode == "on":
        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                for z in range(z_start, z_end+1):
                    grid.add((x, y, z))

    else:
        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                for z in range(z_start, z_end+1):
                    c = (x, y, z)
                    if c in grid:
                        grid.remove((x, y, z))

    return grid


def find_overlap(cube1, cube2):
    x1 = max(cube1['x'][0], cube2['x'][0])
    x2 = min(cube1['x'][1], cube2['x'][1])
    y1 = max(cube1['y'][0], cube2['y'][0])
    y2 = min(cube1['y'][1], cube2['y'][1])
    z1 = max(cube1['z'][0], cube2['z'][0])
    z2 = min(cube1['z'][1], cube2['z'][1])
    # Check if the overlap is valid
    if x1 <= x2 and y1 <= y2 and z1 <= z2:
        return {
            'x': (x1, x2),
            'y': (y1, y2),
            'z': (z1, z2)
        }
    else:
        return None


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    grid = set()
    for line in lines:
        grid = parse_instruction(line, grid)

    return len(grid)


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    cubes = []
    for line in lines:
        # Parse the cube
        (mode, coords) = line.split(" ")
        (xcoords, ycoords, zcoords) = coords.split(",")
        (x_start, x_end) = [int(x) for x in xcoords[2:].split("..")]
        (y_start, y_end) = [int(y) for y in ycoords[2:].split("..")]
        (z_start, z_end) = [int(z) for z in zcoords[2:].split("..")]
        cur_cube = {'x': (x_start, x_end), 'y': (y_start, y_end), 'z': (z_start, z_end)}

        # Find overlap, and add this to the cube list with the negative value.
        # Since we do this for every cube (and overlap!) this will reset the overlap area to a score of 0
        new_cubes = []
        for (c, val) in cubes:
            overlap = find_overlap(cur_cube, c)
            if overlap is not None:
                new_cubes.append((overlap, val*-1))
        cubes.extend(new_cubes)

        # If we are turning lights on, add the new cube with a score of 1
        if mode == "on":
            cubes.append((cur_cube, 1))

    # Scoring
    score = 0
    for (c, val) in cubes:
        s = 1
        for dim in c:
            s *= abs(c[dim][0]-c[dim][1])+1
        score += s*val

    return score


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