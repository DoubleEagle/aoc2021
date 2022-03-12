input_hex = open('day16_dummyinput.txt').read()

input_hex = "620080001611562C8802118E34"

# h_size = len(input_hex) * 4
#
# input_binary = ( bin(int(input_hex, 16))[2:] ).zfill(h_size)

# print(input_binary)

DETECTED_VERSIONS_SUM = 0


# handles single packet from left to right, recurses for new encountered packet
def handle_packet_new(packet):
    global DETECTED_VERSIONS_SUM
    print('------------- handling....', packet)
    version_bin = packet[0:3]
    type_bin = packet[3:6]
    content_bin = packet[6:]

    DETECTED_VERSIONS_SUM += int(version_bin, 2)
    print('Added to version sum:', int(version_bin, 2), DETECTED_VERSIONS_SUM)



    type_dec = int(type_bin, 2)
    if type_dec == 4:
        print('type 4', packet, version_bin, type_bin, content_bin)
        return handle_literal_number_content(content_bin)
    else:
        length_type_indicator = int(content_bin[0], 2)
        print('type other', packet)
        if length_type_indicator == 0:
            print(version_bin, type_bin, content_bin[0], content_bin[1:16], content_bin[16:16 + int(content_bin[1:16], 2)])
            return handle_operator_packetlength_content(content_bin)
        elif length_type_indicator == 1:
            print(version_bin, type_bin, content_bin[0], content_bin[1:])
            return handle_operator(content_bin)

    # if rest_of_packet != None:
    #     handle_packet_new(rest_of_packet)










def handle_packet_hex(hex_input):
    h_size = len(hex_input) * 4

    input_binary = (bin(int(hex_input, 16))[2:]).zfill(h_size)
    handle_packet_new(input_binary)


# def handle_packet_bin(bin_input):
#     global DETECTED_VERSIONS_SUM
#     print('handling....', bin_input)
#     version_bin = bin_input[0:3]
#     type_bin = bin_input[3:6]
#     content_bin = bin_input[6:]
#
#     DETECTED_VERSIONS_SUM += int(version_bin, 2)
#
#     print(bin_input, version_bin, type_bin, content_bin)
#
#     type_dec = int(type_bin, 2)
#     if type_dec == 4:
#         handle_literal_number(content_bin)
#     else:
#         handle_operator(content_bin)


def handle_literal_number_content(content):
    result = ''
    packet_end = 0
    for i in range(0, len(content), 5):
        # print(len(content[i:i+5][1:]))
        result = result + content[i:i + 5][1:]
        if content[i] == '0':
            packet_end = i + 5
            break
    print('type 4 detected! result is:', int(result, 2))
    # return content[packet_end:]

    # if len(content[packet_end:]) > 7:
    #     handle_packet_new(content[packet_end:])

    return result, content[packet_end:]


def handle_operator_packetlength_content(content):
    length_of_packets = int(content[1:16], 2)

    subpackets = content[16:16 + length_of_packets]

    handle_packet_new(subpackets)
    handle_packet_new(content[16 + length_of_packets:])


def handle_operator_numberofpackets_content(content):
    number_of_packets = int(content[1:12], 2)

    # for i in range(0, number_of_packets):



def handle_operator(content):
    print('operator detected!')
    length_type_id = content[0]

    if length_type_id == '0':
        # looking of length of subpackets
        length_of_lengthfield = 15

        length_of_packets = int(content[1:length_of_lengthfield + 1], 2)

        subpackets = content[length_of_lengthfield + 1:length_of_lengthfield + 1 + length_of_packets]

        handle_packet_new(subpackets)

        handle_packet_new(content[length_of_lengthfield + 1 + length_of_packets:])

        # print(length_type_id, length_of_lengthfield, length_of_packets, subpackets)

        # content_to_check = subpackets
        # counter = 0
        # while len(content_to_check) > 3 and counter < 10:
        #     print('content to check:', content_to_check)
        #     # find packet end for type 4 packet
        #     if int(content_to_check[3:6], 2) == 4:
        #         print('found subpacket of type 4!')
        #         content_of_subpacket = content_to_check[6:]
        #         print(content_of_subpacket)
        #         for i in range(0, len(content_of_subpacket), 5):
        #             print(i)
        #             if content_of_subpacket[i] == '0':
        #                 handle_packet_bin(content_to_check[:6 + i + 5])
        #                 content_to_check = content_to_check[6 + i + 5:]
        #                 break
        #     elif int(content_to_check[6]) == '0':
        #         print('found operator subpacket!')
        #         # TODO
        #
        #     counter += 1
    else:
        # looking for number of subpackets
        length_of_lengthfield = 11

        number_of_subpackets = int(content[1:length_of_lengthfield + 1], 2)
        print('number of subpackets:', number_of_subpackets)

        content_to_check = content[length_of_lengthfield + 1:]
        print(content_to_check)

        for i in range(0, number_of_subpackets):
            if int(content_to_check[3:6], 2) == 4:
                print('found subpacket of type 4!')
                content_of_subpacket = content_to_check[6:]
                print(content_of_subpacket)
                for i in range(0, len(content_of_subpacket), 5):
                    # print(i)
                    if content_of_subpacket[i] == '0':
                        handle_packet_new(content_to_check[:6 + i + 5])
                        content_to_check = content_to_check[6 + i + 5:]
                        break
            else:
                print('found operator subpacket!')
                handle_packet_new(content_to_check)
                # TODO






# def handle_bin_content_type_3(content):
#     print('type 3 detected! Looking for number of packets')
#     length_type_id = content[0]
#
#     if length_type_id == '0':
#         length_of_lengthfield = 15
#     else:
#         length_of_lengthfield = 11
#
#



handle_packet_hex(input_hex)


print('Total version number (part 1):', DETECTED_VERSIONS_SUM)