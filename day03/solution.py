from utils.file import read_file_content
from utils.list import deep_copy


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    total = len(lines)

    r1 = ""
    r2 = ""
    for i in range(len(lines[0])):
        ones = len([l for l in lines if l[i] == '1'])
        if ones >= total/2:
            r1 += '1'
            r2 += '0'
        else:
            r1 += '0'
            r2 += '1'

    return int(r1, 2)*int(r2, 2)


def solve_part2(input: str) -> int:
    lines = input.split("\n")

    oxList = deep_copy(lines)
    coList = deep_copy(lines)

    for i in range(len(lines[0])):
        o1 = len([l for l in oxList if l[i] == '1'])
        o2 = len([l for l in coList if l[i] == '1'])

        if len(oxList) > 1:
            if o1 >= len(oxList)/2:
                oxList = [l for l in oxList if l[i] == '1']
            else:
                oxList = [l for l in oxList if l[i] == '0']

        if len(coList) > 1:
            if o2 >= len(coList)/2:
                coList = [l for l in coList if l[i] == '0']
            else:
                coList = [l for l in coList if l[i] == '1']

    return int(oxList[0], 2) * int(coList[0], 2)


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

# I knew there was a better way to count/filter lists in Python, but in the moment did not think of it.
# So once it was done i wanted to refresh my memory, and implemented it with better list manipulation.
# These are the original methods as backup

# def solve_part1(input: str) -> int:
#     lines = input.split("\n")
#     numLines = len(lines)
#
#     occ = [0]*len(lines[0])
#     for l in lines:
#         for i in range(len(l)):
#             if l[i] == '1':
#                 occ[i] += 1
#
#     r1 = ""
#     r2 = ""
#     for o in occ:
#         if o >= numLines/2:
#             r1 += '1'
#             r2 += '0'
#         else:
#             r1 += '0'
#             r2 += '1'
#
#     num1 = int(r1, 2)
#     num2 = int(r2, 2)
#
#     return num1*num2

# def solve_part2(input: str) -> int:
#     lines = input.split("\n")
#
#     oxList = deep_copy(lines)
#     coList = deep_copy(lines)
#
#     oxResult = None
#     coResult = None
#
#     for i in range(len(lines[0])):
#         o1 = count_ones(oxList, i)
#         o2 = count_ones(coList, i)
#         oxToRemove = []
#         coToRemove = []
#         if o1 >= len(oxList)/2:
#             for l in oxList:
#                 if l[i] != '1':
#                     oxToRemove.append(l)
#         else:
#             for l in oxList:
#                 if l[i] != '0':
#                     oxToRemove.append(l)
#
#         if o2 >= len(coList)/2:
#             for l in coList:
#                 if l[i] != '0':
#                     coToRemove.append(l)
#         else:
#             for l in coList:
#                 if l[i] != '1':
#                     coToRemove.append(l)
#
#         if oxResult == None:
#             for l in oxToRemove:
#                 oxList.remove(l)
#             if len(oxList) == 1:
#                 oxResult = oxList[0]
#
#         if coResult == None:
#             for l in coToRemove:
#                 coList.remove(l)
#             if len(coList) == 1:
#                 coResult = coList[0]
#
#     coVal = int(coResult, 2)
#     oxVal = int(oxResult, 2)
#
#     return coVal*oxVal