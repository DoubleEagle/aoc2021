import ast
import math
import re
from termcolor import colored

import numpy as np

input = open('day18_input.txt').read().split('\n')


# print(input[0])


def add_lists(list1, list2):
    return '[' + list1 + ',' + list2 + ']'


def split_string_in_chars_and_numbers(list_string):
    result = []
    prev_number_is_digit = False
    for i in range(0, len(list_string)):
        if list_string[i].isdigit():
            if prev_number_is_digit:
                result[-1] += list_string[i]
                # result.append(list_string[i])
            else:
                result.append(list_string[i])

            prev_number_is_digit = True
        else:
            prev_number_is_digit = False
            result.append(list_string[i])
    return result


# checks if there is a fourth pair somewhere nested and if yes, returns index of first char of that pair
def check_for_four_pairs(pairs):
    counter = 0
    chars = split_string_in_chars_and_numbers(pairs)
    for i in range(0, len(chars)):
        # print(chars[i], counter)
        if chars[i] == '[':
            counter += 1
        elif chars[i] == ']':
            counter -= 1

        if counter == 5:
            return True, i
    return False, 0


def explode(pairs, start_index):
    # convert into list of chars and numbers
    chars = split_string_in_chars_and_numbers(pairs)
    pairs_chars = split_string_in_chars_and_numbers(pairs)
    end_index = pairs_chars.index(']', start_index)
    pair_string = ''.join(pairs_chars[start_index:end_index + 1])
    pair_numbers = list(map(int, pair_string[1:-1].split(',')))
    # print(pair_string, pair_numbers, pairs, start_index, end_index)

    # add number to left
    left_number_index = -1

    for i in reversed(range(0, start_index)):
        if chars[i].isdigit():
            left_number_index = i
            break

    if left_number_index >= 0:
        new_left_number = int(pairs_chars[left_number_index]) + pair_numbers[0]
        pairs_chars[left_number_index] = str(new_left_number)

    # add number to right
    right_number_index = -1

    for i in range(end_index, len(chars)):
        if chars[i].isdigit():
            right_number_index = i
            break

    if right_number_index >= 0:
        new_right_number = int(pairs_chars[right_number_index]) + pair_numbers[1]
        pairs_chars[right_number_index] = str(new_right_number)

    # replace with 0
    pairs = ''.join(pairs_chars)
    pairs_second_part = pairs[start_index:]

    pairs_second_part = pairs_second_part.replace(pair_string, '0', 1)

    pairs = pairs[:start_index] + pairs_second_part

    #
    #
    #
    #
    # # find number left of left number and add it if there's one
    # # search from right to left and only stop when all digits are found
    # # TODO: probably should use regex for this or smth
    #
    #
    #
    #
    # # update values because shit has been deleted
    #
    #
    #
    # end_index = pairs.find(']', start_index)
    # pair_string = pairs[start_index:end_index + 1]
    # pair_numbers = list(map(int, pairs[start_index + 1:end_index].split(',')))
    #
    # pairs = explode_to_left(pairs, start_index)
    #
    # end_index = pairs.find(']', start_index)
    # # pair_string = pairs[start_index:end_index + 1]
    # # pair_numbers = list(map(int, pairs[start_index + 1:end_index].split(',')))
    # pairs_chars = list(pairs)
    #
    # # TODO: probably should use regex for this or smth
    # start_right_number = -1
    # end_right_number = -1
    #
    # for i in range(end_index, len(pairs_chars)):
    #     # print(i)
    #     if pairs_chars[i].isdigit() and start_right_number < 0:
    #         start_right_number = i
    #         end_right_number = i + 1
    #     elif pairs_chars[i].isdigit() and start_right_number > 0:
    #         end_right_number = i + 1
    #     elif start_right_number > 0:
    #         break
    #
    # if start_right_number >= 0:
    #     new_right_number = int(pairs[start_right_number:end_right_number])
    #     pairs_chars[start_right_number] = str(int(new_right_number + pair_numbers[1]))
    #     del pairs_chars[start_right_number + 1:end_right_number]
    #
    # # print(start_right_number, end_right_number)
    #
    # # add numbers to neighbours
    #
    # pairs = ''.join(pairs_chars)
    #
    # # remove pair and replace it with 0
    # pairs = pairs.replace(pair_string, '0', 1)

    return pairs


def check_for_splits(pairs):
    pairs_chars = list(pairs)

    number_evaluating = None
    for i in range(0, len(pairs_chars)):
        if pairs_chars[i].isdigit():
            if number_evaluating is None:
                number_evaluating = pairs_chars[i]
            else:
                number_evaluating = number_evaluating + pairs_chars[i]
        else:
            if number_evaluating is not None:
                if int(number_evaluating) > 9:
                    return True, number_evaluating
            number_evaluating = None
    return False, 0


def split(pairs, number):
    number_int = int(number)

    left_number = math.floor(number_int / 2)
    right_number = math.ceil(number_int / 2)

    # print(left_number, right_number)

    new_pair_string = '[' + str(left_number) + ',' + str(right_number) + ']'

    pairs = pairs.replace(number, new_pair_string, 1)

    return pairs


def magnitude(pairs):
    # print('----- doing magnitude calc over', pairs)
    mag = 0
    # find pair
    m = re.search(r'\[[0-9]+,[0-9]+\]', pairs)

    if m:
        pair_found = m.group(0)
        # print(pair_found, pairs)
        numbers = list(map(int, pair_found[1:-1].split(',')))
        mag_of_pair = 3 * numbers[0] + 2 * numbers[1]
        pairs = pairs.replace(pair_found, str(mag_of_pair))
        return magnitude(pairs)
    else:
        return int(pairs)


def find_highest_additive_magnitude(input_list):
    highest_mag = 0

    for input in input_list:
        for input2 in input_list:
            if input != input2:
                print('checking... ', input, 'against', input2)
                mag = magnitude(reduce(add_lists(input, input2)))
                highest_mag = max(mag, highest_mag)
                print('checking... ', input2, 'against', input)
                mag = magnitude(reduce(add_lists(input2, input)))
                highest_mag = max(mag, highest_mag)

                # do additionblabla
                # reduce
                # get magnitude
                # if groter, doe toevoegen aan lijst
    # doe resultaat returnen
    return highest_mag



def check_if_correct_list(pairs):
    ast.literal_eval(pairs)


def print_pretty(pairs, startindex=None, number=None):
    if startindex is not None:
        pair_chars = split_string_in_chars_and_numbers(pairs)
        print(''.join(pair_chars[:startindex]), end='')
        print(colored(''.join(pair_chars[startindex:pair_chars.index(']', startindex) + 1]), 'red'), end='')
        print(''.join(pair_chars[pair_chars.index(']', startindex) + 1:]))
    if number is not None:
        print(pairs[:pairs.find(number)], end='')
        print(colored(number, 'red'), end='')
        print(pairs[pairs.find(number) + len(number):])


def reduce(result):
    while True:
        contains_fourth_pair, index_nested_pair = check_for_four_pairs(result)
        contains_big_number, number = check_for_splits(result)
        if contains_fourth_pair:
            # print('------ Fifth pair found, new pair list:', end=' ')
            # print_pretty(result, startindex=index_nested_pair)
            result = explode(result, index_nested_pair)
            check_if_correct_list(result)
        elif contains_big_number:
            # print('------ Split found, new pair list:     ', end=' ')
            # print_pretty(result, number=number)
            result = split(result, number)
            check_if_correct_list(result)
        else:
            break

    return result



# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"))

# input = ['[[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]']
#

# input = '[[[[6,7],[0,7]],[[7,[6,7]],[0,21]]],[[2,[11,10]],[[0,8],[8,0]]]]'
# #
# print(input)
# # splitttt = split(input, '20')
# # print(check_for_four_pairs(input))
# print(explode(input, check_for_four_pairs(input)[1]))
# exit()


# result = ''
# for line in input:
#     if result == '':
#         result = line
#     else:
#         result = add_lists(result, line)
#
#     print('---------------------------- Evaluating', result)
#
#     result = reduce(result)
#
# print('Part 1:', result)
# print(magnitude(result))

print(find_highest_additive_magnitude(input))