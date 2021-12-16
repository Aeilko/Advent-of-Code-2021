from utils.file import read_file_content


HEX = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}


def parse_input(input):
    result = ""
    for x in input:
        result += HEX[x]
    return result


def parse_packets(bits, num_packets=-1):
    start = 0
    result = []
    while len(bits)-start >= 8:
        packet = {
            'V': int(bits[start:start+3], 2),
            'T': int(bits[start+3:start+6], 2)
        }
        start += 6
        if packet['T'] == 4:
            val = ""
            for i in range(len(bits)):
                sign_bit = bits[start]
                val += bits[start+1:start+5]
                start += 5
                if sign_bit == '0':
                    break
            packet['value'] = int(val, 2)
        else:
            packet['I'] = bits[start]
            start += 1
            if packet['I'] == '0':
                packet['L'] = int(bits[start:start+15], 2)
                start += 15
                packet['packets'], pl = parse_packets(bits[start:start+packet['L']])
                start += packet['L']
            elif packet['I'] == '1':
                packet['L'] = int(bits[start:start+11], 2)
                start += 11
                packet['packets'], pl = parse_packets(bits[start:], num_packets=packet['L'])
                start += pl

        result.append(packet)

        if len(result) == num_packets:
            break

    return result, start


def version_sum(packet):
    result = packet['V']
    if "packets" in packet:
        for p in packet['packets']:
            result += version_sum(p)
    return result


def packet_value(packet):
    result = 0
    if packet['T'] == 0:
        for p in packet['packets']:
            result += packet_value(p)
    elif packet['T'] == 1:
        prod = 1
        for p in packet['packets']:
            prod *= packet_value(p)
        result += prod
    elif packet['T'] == 2:
        vals = []
        for p in packet['packets']:
            vals.append(packet_value(p))
        result += min(vals)
    elif packet['T'] == 3:
        vals = []
        for p in packet['packets']:
            vals.append(packet_value(p))
        result += max(vals)
    elif packet['T'] == 4:
        result += packet['value']
    elif packet['T'] == 5:
        v1 = packet_value(packet['packets'][0])
        v2 = packet_value(packet['packets'][1])
        if v1 > v2:
            result += 1
    elif packet['T'] == 6:
        v1 = packet_value(packet['packets'][0])
        v2 = packet_value(packet['packets'][1])
        if v1 < v2:
            result += 1
    elif packet['T'] == 7:
        v1 = packet_value(packet['packets'][0])
        v2 = packet_value(packet['packets'][1])
        if v1 == v2:
            result += 1
    return result


def solve_part1(input: str) -> int:
    bits = parse_input(input)
    packet, length = parse_packets(bits)
    return version_sum(packet[0])


def solve_part2(input: str) -> int:
    bits = parse_input(input)
    packet, length = parse_packets(bits)
    return packet_value(packet[0])


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