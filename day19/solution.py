from utils.file import read_file_content


def known_node_list(nodes):
    result = {}
    result_sorted = {}
    for n in nodes:
        all = []
        all_sorted = []
        for n2 in nodes:
            if n == n2:
                continue
            d1 = []
            d2 = []
            for i in range(3):
                d1.append(n[i]-n2[i])
                d2.append(abs(n[i]-n2[i]))
            all.append(d1)
            d2.sort()
            all_sorted.append(d2)
        result[n] = all
        result_sorted[n] = all_sorted

    return result, result_sorted


def compare_known_node_lists(list1, list2):
    matches = 0
    for n1 in list1:
        if n1 in list2:
            matches += 1
    return matches


def apply_mapping(node, mapping, offset=None):
    result = [0]*len(node)
    for i in range(len(node)):
        if mapping[i][-1] == "x":
            result[i] = node[0]
        elif mapping[i][-1] == "y":
            result[i] = node[1]
        elif mapping[i][-1] == "z":
            result[i] = node[2]

        if mapping[i][0] == '-':
            result[i] *= -1

        if offset is not None:
            result[i] += offset[i]
    return tuple(result)


def find_locations(input):
    # Parse input
    groups = input.split("\n\n")
    scanners = [None] * len(groups)
    for s in groups:
        beacons = s.split("\n")
        id = int(beacons[0][12:-4])
        nodes = []
        for b in beacons[1:]:
            (x, y, z) = [int(a) for a in b.split(",")]
            nodes.append((x, y, z))
        scanners[id] = nodes

    # Keep track of the beacons of which we know the absolute position (to scanner 0)
    node_list, sorted_list = known_node_list(scanners[0])
    confirmed_beacons = set()
    confirmed_beacons_list = {}
    confirmed_beacons_sorted = {}
    for n in scanners[0]:
        confirmed_beacons.add(n)
        confirmed_beacons_list[n] = node_list[n]
        confirmed_beacons_sorted[n] = sorted_list[n]

    # Start trying to match scanners to the set of known beacons
    s_done = set([0])
    scanner_mappings = {0: ["x", "y", "z"]}
    scanner_offsets = {0: (0, 0, 0)}
    while True:
        for i in range(len(scanners)):
            if i in s_done:
                continue

            s = scanners[i]
            b_list, b_list_sorted = known_node_list(s)
            matching_beacons = []
            # See if we can find a beacon which distances matches with a known beacon
            for beacon in b_list:
                for cbeacon in confirmed_beacons_list:
                    matches = compare_known_node_lists(b_list_sorted[beacon], confirmed_beacons_sorted[cbeacon])
                    if matches >= 11:
                        matching_beacons.append(cbeacon)
                        matching_beacons.append(beacon)
                        break
                if len(matching_beacons) > 0:
                    break

            # Found a matching beacon
            if len(matching_beacons) > 0:
                confirmed_list = confirmed_beacons_list[matching_beacons[0]]
                matching_list = b_list[matching_beacons[1]]
                coord1 = None
                coord2 = None
                # Find 2 matching distances, which all have unique values
                for c1 in confirmed_list:
                    if c1[0] == c1[1] or c1[0] == c1[2] or c1[1] == c1[2]:
                        continue
                    for c2 in matching_list:
                        r = True
                        for x in c1:
                            if x not in c2 and x * -1 not in c2:
                                r = False
                                break
                        if r:
                            coord1 = c1
                            coord2 = c2
                            break
                    if coord1 is not None:
                        break

                # Determine the mapping of these distances
                mapping = []
                for c in coord1:
                    map = ""
                    if c not in coord2:
                        c *= -1
                        map += "-"
                    if coord2[0] == c:
                        map += "x"
                    elif coord2[1] == c:
                        map += "y"
                    elif coord2[2] == c:
                        map += "z"
                    mapping.append(map)
                scanner_mappings[i] = mapping

                # Find the offset (scanner location)
                n1 = matching_beacons[0]
                n2 = apply_mapping(matching_beacons[1], mapping)
                offset = (n1[0] - n2[0], n1[1] - n2[1], n1[2] - n2[2])
                scanner_offsets[i] = offset

                # Apply mapping on nodes
                for n in s:
                    new_node = apply_mapping(n, mapping, offset)
                    confirmed_beacons.add(new_node)

                # Recalculate known distance lists, this is probably pretty expensive to make and search. But it seems
                # like the easier than coming up with a smart solution
                confirmed_beacons_list, confirmed_beacons_sorted = known_node_list(confirmed_beacons)

                s_done.add(i)

        if len(s_done) == len(scanners):
            break

    return confirmed_beacons, scanner_offsets


def solve_part1(input: str) -> int:
    beacons, scanners = find_locations(input)
    return len(beacons)


def solve_part2(input: str) -> int:
    beacons, scanners = find_locations(input)

    distances = set()
    for s1 in scanners:
        s1 = scanners[s1]
        for s2 in scanners:
            s2 = scanners[s2]
            if s1 == s2:
                continue

            d = abs(s1[0]-s2[0]) + abs(s1[1]-s2[1]) + abs(s1[2]-s2[2])
            distances.add(d)

    return max(distances)


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