import math

from utils.file import read_file_content
from utils.tree import BinaryTreeNode, NextLeafRight, NextLeafLeft


def parse_input(input):
    cur_node = BinaryTreeNode()
    cur_side = "left"
    for c in input[1:-1]:
        if c == "[":
            new_node = BinaryTreeNode(parent=cur_node)
            if cur_side == "left":
                cur_node.left = new_node
            elif cur_side == "right":
                cur_node.right = new_node
            cur_node = new_node
            cur_side = "left"
        elif c == "]":
            cur_node = cur_node.parent
        elif c == ",":
            cur_side = "right"
        else:
            if cur_side == "left":
                cur_node.left = int(c)
            else:
                cur_node.right = int(c)

    return cur_node


def add_nodes(n1, n2):
    root = BinaryTreeNode(left=n1, right=n2)
    n1.parent = root
    n2.parent = root
    return root


def reduce(node):
    root = node

    while True:
        cur_node = root
        depth = 0
        explode = False

        # Go to leftmost leaf
        while type(cur_node.left) == BinaryTreeNode:
            cur_node = cur_node.left
            depth += 1

        # Check for explodes
        while cur_node is not None:
            if type(cur_node.left) != BinaryTreeNode and type(cur_node.right) != BinaryTreeNode and depth == 4:
                # print("Explode", cur_node)
                # print(cur_node, depth)
                val, left_node, left_depth = NextLeafLeft(cur_node, depth)
                # print(val, left_node, left_depth)
                if left_node is not None:
                    if type(left_node.right) == BinaryTreeNode:
                        left_node.left += cur_node.left
                    else:
                        left_node.right += cur_node.left
                val, right_node, right_depth = NextLeafRight(cur_node, depth)
                # print(val, right_node, right_depth)
                if right_node is not None:
                    if type(right_node.left) == BinaryTreeNode:
                        right_node.right += cur_node.right
                    else:
                        right_node.left += cur_node.right

                prev = cur_node
                cur_node = cur_node.parent
                depth -= 1
                if cur_node.left == prev:
                    cur_node.left = 0
                else:
                    cur_node.right = 0

                explode = True
                break
            else:
                val, cur_node, depth = NextLeafRight(cur_node, depth)
                # print(val, cur_node, depth)

        if explode:
            continue

        cur_node = root
        depth = 0
        split = False
        # Go to leftmost leaf
        while type(cur_node.left) == BinaryTreeNode:
            cur_node = cur_node.left
            depth += 1

        # Check for splits
        while cur_node is not None:
            if type(cur_node.left) == int and cur_node.left >= 10:
                # print("Split", cur_node)
                l = math.floor(cur_node.left/2)
                r = math.ceil(cur_node.left/2)
                cur_node.left = BinaryTreeNode(left=l, right=r, parent=cur_node)
                split = True
                break

            if type(cur_node.right) == int and cur_node.right >= 10:
                # print("Split", cur_node)
                l = math.floor(cur_node.right / 2)
                r = math.ceil(cur_node.right / 2)
                cur_node.right = BinaryTreeNode(left=l, right=r, parent=cur_node)
                split = True
                break

            val, cur_node, depth = NextLeafRight(cur_node, depth)

        if not explode and not split:
            break

    return root


def magnitude(node):
    if type(node) == int:
        return node
    else:
        return 3*magnitude(node.left) + 2*magnitude(node.right)


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    cur_tree = parse_input(lines[0])
    for line in lines[1:]:
        tree = parse_input(line)
        cur_tree = add_nodes(cur_tree, tree)
        cur_tree = reduce(cur_tree)

    return magnitude(cur_tree)


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    trees = []
    for line in lines:
        trees.append(parse_input(line))

    scores = set()
    for i in range(len(trees)):
        for j in range(len(trees)):
            if i == j:
                continue

            # Reload the trees, because our methods update the trees and i dont feel like writing deepcopy methods
            t1 = parse_input(lines[i])
            t2 = parse_input(lines[j])

            tree = reduce(add_nodes(t1, t2))
            scores.add(magnitude(tree))

    return max(scores)


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