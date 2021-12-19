import operator
from functools import reduce

input_hex = open('day16_input.txt').read().split('\n')

DETECTED_VERSIONS_SUM = 0


def convert_hex_to_bin(hex_input):
    print('Hex input:', hex_input)
    h_size = len(hex_input) * 4
    return (bin(int(hex_input, 16))[2:]).zfill(h_size)


def handle_literal(literal_packet_content):
    result = ''
    packet_end = 0
    for i in range(0, len(literal_packet_content), 5):
        # print(len(content[i:i+5][1:]))
        result = result + literal_packet_content[i:i + 5][1:]
        if literal_packet_content[i] == '0':
            packet_end = i + 5
            break
    print('type 4 detected! result is:', int(result, 2))

    return int(result, 2), literal_packet_content[packet_end:]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def handle_packet(packet):
    global DETECTED_VERSIONS_SUM
    print('------------- handling....', packet)
    version = int(packet[0:3], 2)
    type = int(packet[3:6], 2)
    content = packet[6:]

    DETECTED_VERSIONS_SUM += version
    print('Added to version sum:', version, DETECTED_VERSIONS_SUM)

    literals = []

    print(version, type, content)

    # Found literal
    if type == 4:
        print('Is literal packet...')
        literal, rest = handle_literal(content)
        literals.append(literal)
        return literal, rest


    # Found operator
    length_type = int(packet[6])

    if length_type == 0:
        print('Is operator packet with fixed length...')
        length = int(packet[7:7+15], 2)
        subpackets = packet[7+15:7+15+length]
        # rest = packet[7+15+length:]
        while len(subpackets):
            literal, subpackets = handle_packet(subpackets)
            literals.append(literal)
        to_return = packet[7+15+length:]
    else:
        number_of_subpackets = int(packet[7:7+11], 2)
        subpackets = packet[7+11:]
        print('Is operator packet with', number_of_subpackets, 'subpackets...')
        for i in range(number_of_subpackets):
            literal, subpackets = handle_packet(subpackets)
            literals.append(literal)
        to_return = subpackets

    if type == 0:
        print('SUUUUMMMMMMMMM', literals)
        return sum(literals), to_return

    if type == 1:
        return prod(literals), to_return

    if type == 2:
        return min(literals), to_return

    if type == 3:
        return max(literals), to_return

    if type == 5:
        print('============== TYPE 5 literals:', literals)
        return 1 if literals[0] > literals[1] else 0, to_return

    if type == 6:
        print('============== TYPE 6 literals:', literals)
        return 1 if literals[0] < literals[1] else 0, to_return

    if type == 7:
        print('============== TYPE 7 literals:', literals)
        return 1 if literals[0] == literals[1] else 0, to_return


print(handle_packet(convert_hex_to_bin(input_hex[0])))

print('sum of versions:', DETECTED_VERSIONS_SUM)