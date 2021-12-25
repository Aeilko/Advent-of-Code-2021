import copy
import math
from collections import deque

from utils.file import read_file_content


# Program is a loop with 3 values which can differ (a, b, c)
# w = int(input())
# x = ((z%26) + b) != w
# z = floor(z/a)
# z = z * (25x + 1) (either z * 26 or z * 1)
# z = z + (w+c)x
#
# x and y get reset every 'round' and z is some output sum (which we should get to 0)
# a can only be 1 or 26, both occur 7 times
# z is multiplied by 26 if the input does not equal z%26 + b
# So if thats not the case, z stays the same
# If we can keep x at 0 our output will stay at 0 (but that only works if we need to find ANY value that results in 0)
# If we multiply z by 26, and then add the value of (w+c)x, this value ((w+c)x) is used in the next iteration at z%26
# z/a, for a = 26 removes this value ((w+c)x) from the z
# We are adding and removing values (between 0 and 25) from z
# Add a value:                   z = z*26 + val
# Remove a value:                z = z/26
# View the current value:        val = z%26
#
# New program
# w = int(input())
# x = b+cur_value != w
# z = z/a   => Possibly pop the value from the stack, we have no influence over a.
# if x
#   Push new value w+c on stack
# else
#   Do nothing
#
# z starts at 0, there are 7 pops and pushes (the a values), so if we do not perform any additional pushes we are fine
# So we are back at the 'x should always be 0' statement, which doesnt work since our first x can't be 0
# That's incorrect, there are 7 pushes and 7 pops, but the first of these 7 pushes is pushing 0 (the first round)
# So we can push one additional value, which will be the first round, all other rounds should result in x == 0
# x == 0 is not always possible (as in the first round), so we should find the largest first digit for which all
# other digits are able to set x == 0


VARS = {'w', 'x', 'y', 'z'}


def run_aclu(program, inputs=None):
    if type(program) == str:
        operations = program.split("\n")
    else:
        operations = program
    input_pointer = 0
    memory = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for operation in operations:
        params = operation.split(" ")
        # Convert 2nd parameter to an integer
        if len(params) > 2:
            if params[2] not in VARS:
                params[2] = int(params[2])
            else:
                params[2] = memory[params[2]]

        if params[0] == "inp":
            if inputs is None:
                # Request user input
                inp = 0
                while inp == 0:
                    print("Input: ", end='')
                    val = input()
                    if len(val) != 1:
                        print("Please provide a single digit")
                    else:
                        try:
                            inp = int(val)
                            memory[params[1]] = inp
                        except ValueError as e:
                            print("That's not a digit")
                            inp = 0

                memory[params[1]] == inp
            else:
                # Full input is provided, use the next value
                memory[params[1]] == int(inputs[input_pointer])
                input_pointer += 1
        elif params[0] == "add":
            memory[params[1]] += params[2]
        elif params[0] == "mul":
            memory[params[1]] *= params[2]
        elif params[0] == "div":
            memory[params[1]] = math.floor(memory[params[1]]/params[2])
        elif params[0] == "mod":
            memory[params[1]] = memory[params[1]] % params[2]
        elif params[0] == "eql":
            memory[params[1]] = 1 if memory[params[1]] == params[2] else 0
        else:
            print("Unknown instruction: '" + params[0] + "'")

    return memory


def parse_input(input):
    rounds = input.split("\ninp w\n")
    result = []
    found_add_y_w = False
    for r in rounds:
        vals = {}
        lines = r.split("\n")
        for line in lines:
            params = line.split(" ")
            if params[0] == "div" and params[1] == "z":
                vals['a'] = int(params[2])
            elif params[0] == "add" and params[1] == "x" and params[2] != "z":
                vals['b'] = int(params[2])
            elif params[0] == "add" and params[1] == "y" and params[2] == "w":
                found_add_y_w = True
            elif params[0] == "add" and params[1] == "y" and found_add_y_w:
                vals['c'] = int(params[2])
        result.append(vals)
    return result


def find_max_value(stack, round, program):
    if round == len(program):
        return ""
    if program[round]['a'] == 26:
        # We have to meet x == 0
        val = stack.pop() % 26
        val += program[round]['b']
        if val < 1 or val > 9:
            # We cannot equal this value
            return None
        else:
            r = find_max_value(stack, round+1, program)
            if r is None:
                return None
            else:
                return str(val) + r
    else:
        # We don't have to meet x == 0, so find the highest value for which the rest is possible
        for i in range(9, 0, -1):
            sc = copy.deepcopy(stack)
            sc.append(i + program[round]['c'])
            r = find_max_value(sc, round+1, program)
            if r is not None:
                return str(i) + r
        return None


def find_min_value(stack, round, program):
    if round == len(program):
        return ""
    if program[round]['a'] == 26:
        # We have to meet x == 0
        val = stack.pop() % 26
        val += program[round]['b']
        if val < 1 or val > 9:
            # We cannot equal this value
            return None
        else:
            r = find_min_value(stack, round+1, program)
            if r is None:
                return None
            else:
                return str(val) + r
    else:
        # We don't have to meet x == 0, so find the highest value for which the rest is possible
        for i in range(1, 10):
            sc = copy.deepcopy(stack)
            sc.append(i + program[round]['c'])
            r = find_min_value(sc, round+1, program)
            if r is not None:
                return str(i) + r
        return None


def solve_part1(inp: str) -> int:
    program = parse_input(inp)
    stack = deque()
    val = int(find_max_value(stack, 0, program))
    return val


def solve_part2(inp: str) -> int:
    program = parse_input(inp)
    stack = deque()
    val = int(find_min_value(stack, 0, program))
    return val


def test_part1():
    i = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(i)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    i = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(i)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    i = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    # test_part1()
    print("Part 1 result:\t" + str(solve_part1(i)))

    print("\n --- Part 2 ---")
    # test_part2()
    print("Part 2 result:\t" + str(solve_part2(i)))
