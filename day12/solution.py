from utils.file import read_file_content


def find_paths(cur_node, graph, path):
    path.append(cur_node)
    routes = set()
    if cur_node == "end":
        routes.add(tuple(path))
    else:
        neighbours = graph[cur_node]
        for n in neighbours:
            if n.islower():
                if n not in path:
                    routes = routes | find_paths(n, graph, list(path))
            else:
                routes = routes | find_paths(n, graph, list(path))

    return routes


def find_paths2(cur_node, graph, path, double_visited):
    path.append(cur_node)
    routes = set()
    if cur_node == "end":
        routes.add(tuple(path))
    else:
        neighbours = graph[cur_node]
        for n in neighbours:
            if n.islower():
                if n not in path:
                    routes = routes | find_paths2(n, graph, list(path), double_visited)
                elif not double_visited and n != "start":
                    routes = routes | find_paths2(n, graph, list(path),  True)
            else:
                routes = routes | find_paths2(n, graph, list(path), double_visited)

    return routes


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    graph = {}
    for line in lines:
        (n1, n2) = line.split("-")
        if n1 in graph:
            graph[n1].add(n2)
        else:
            graph[n1] = {n2}
        if n2 in graph:
            graph[n2].add(n1)
        else:
            graph[n2] = {n1}

    routes = find_paths("start", graph, [])

    return len(routes)


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    graph = {}
    for line in lines:
        (n1, n2) = line.split("-")
        if n1 in graph:
            graph[n1].add(n2)
        else:
            graph[n1] = {n2}
        if n2 in graph:
            graph[n2].add(n1)
        else:
            graph[n2] = {n1}

    routes = find_paths2("start", graph, [], False)

    return len(routes)


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