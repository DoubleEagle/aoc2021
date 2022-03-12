from collections import Counter

import pandas as pd
import numpy as np
import copy

input_file = open('day3_input.txt')

lines = input_file.read().split('\n')
NUMBER_LEN = len(lines[0])

lines_array = [[] for i in range(len(lines))]

# ugly way to get it to chars
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        lines_array[i].append(lines[i][j])


df = pd.DataFrame(lines_array)
print(df)


def get_most_occuring_at_pos(dataframe, position, oxygen=True):
    occurrences = dataframe[position].mode()
    if len(occurrences) > 1:
        if oxygen == True:
            return '1'
    return dataframe[position].value_counts().idxmax()


def get_oxygen_gen_rating(dataframe):
    leftovers = dataframe.copy(deep=True)
    for i in range(NUMBER_LEN):
        if len(leftovers.index_nested_pair) == 1:
            return leftovers
        most_occuring = get_most_occuring_at_pos(leftovers, i)
        leftovers = leftovers.drop(leftovers[leftovers[i] != most_occuring].index_nested_pair)
        # yea let's check this twice because why not
        if len(leftovers.index_nested_pair) == 1:
            return int(''.join(leftovers.to_numpy()[0]), 2)


def get_co2_scrub_rating(dataframe):
    leftovers = dataframe.copy(deep=True)
    for i in range(NUMBER_LEN):
        if len(leftovers.index_nested_pair) == 1:
            return leftovers
        most_occuring = get_most_occuring_at_pos(leftovers, i)
        if most_occuring == '1':
            least_occuring = '0'
        else:
            least_occuring = '1'
        leftovers = leftovers.drop(leftovers[leftovers[i] != least_occuring].index_nested_pair)
        # yea let's check this twice because why not
        if len(leftovers.index_nested_pair) == 1:
            return int(''.join(leftovers.to_numpy()[0]), 2)


print(get_oxygen_gen_rating(df) * get_co2_scrub_rating(df))

# occurences_1 = [0] * len(lines[0])
# occurences_0 = [0] * len(lines[0])
#
# for line in lines:
#     for i in range(0, len(line)):
#         if line[i] == '1':
#             occurences_1[i] += 1
#         elif line[i] == '0':
#             occurences_0[i] += 1
#
#
# half = len(lines) / 2
# output = ''
# for i in range(0, len(occurences_1)):
#     if int(occurences_0[i]) > half:
#         output = output + '0'
#     else:
#         output = output + '1'
#
#
# output_gamma = int(output, 2)
# output_epsilon = int(''.join('1' if x == '0' else '0' for x in output), 2)
#
# def find_most_occuring_in_position(numbers, position):
#     found = []
#     for number in numbers:
#         found.append(int(number[position]))
#     occurence_count = Counter(found)
#     print('found in pos ', position, found, occurence_count.most_common(1)[0][0])
#     return occurence_count.most_common(1)[0][0]
#
#
# def find_oxygen_generator_rating(bin_numbers, most_occuring):
#     # leftovers = bin_numbers.deepcopy()
#     leftovers = copy.deepcopy(bin_numbers)
#
#     for i in range(0, len(bin_numbers[0])):
#         print(leftovers)
#         most_common = find_most_occuring_in_position(leftovers, i)
#         if len(leftovers) == 1:
#             print('return!')
#             return leftovers
#         temp = copy.deepcopy(leftovers)
#         for bin_number in leftovers:
#             # print(bin_number, bin_number[i], temp)
#             if int(bin_number[i]) != int(most_common):
#                 print('remove', bin_number, bin_number[i], most_common)
#                 temp.remove(bin_number)
#         leftovers = temp
#
#
# # print(output_gamma * output_epsilon)
# #
# # print(occurences_0, occurences_1)
#
# # print('occurences', output)
# print(find_oxygen_generator_rating(lines, output))
#
# # print(find_most_occuring_in_position(lines, 0))