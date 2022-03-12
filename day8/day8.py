import itertools

import numpy as np
import pandas as pd

number_segments = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

lines = list(map(lambda line: list(map(lambda words: words.split(' '), line.split(' | '))), open('day8_input.txt').read().split('\n')))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# solutions = pd.DataFrame(data = [[1 for i in range(0, 7)] for j in range(0, 7)], index=letters, columns=letters)
solutions = [[1 for i in range(0, 7)] for j in range(0, 7)]


def letter_x_can_be_y(solutions, array_observation, array_options):
    for x in array_observation:
        for y in letters:
            if y not in array_options:
                solutions[letters.index(x)][letters.index(y)] = 0
    return solutions


def check_for_row_pairs(solutions, checked=[]):
    rows_with_2s = []
    rows_with_2s_indexes = []
    for i in range(0, len(solutions)):
        row = solutions[i]
        if sum(row) == 2 and i not in checked:
            rows_with_2s.append(row)
            rows_with_2s_indexes.append(i)

    if len(rows_with_2s) > 1:
        if rows_with_2s[0] == rows_with_2s[1]:
            checked.append(rows_with_2s_indexes[0])
            checked.append(rows_with_2s_indexes[1])
            positions_to_remove = [i for i, x in enumerate(rows_with_2s[0]) if x == 1]
            for row in solutions:
                if row != rows_with_2s[0]:
                    for i in range(0, 7):
                        if i in positions_to_remove:
                            row[i] = 0

            solutions = check_for_row_pairs(solutions, checked)

    return solutions


def check_for_singles(solutions):
    singles = []
    for row in solutions:
        if sum(row) == 1:
            singles.append([row.index_nested_pair(1), row])

    for single_index, row in singles:
        for s_row in solutions:
            if row != s_row:
                s_row[single_index] = 0

    return solutions


def make_sense_of_numbers(solutions, words):
    words_letterlist = list(map(lambda x: sorted(list(x)), words))
    numbers = ''

    for word in words_letterlist:
        letter_options = []
        for letter in word:
            letter_options.append([letters[i] for i, x in enumerate(solutions[letters.index(letter)]) if x == 1])
        word_options = list(itertools.product(*letter_options))
        word_options_sorted = list(map(lambda x: sorted(x), word_options))
        number = []
        number_options = []
        for i in range(0, len(word_options)):
            for key, value in number_segments.items():
                if value == word_options_sorted[i]:
                    number.append(key)
                    number_options.append(value)
        numbers += str(number[0])

    # print('results is', int(numbers))
    return int(numbers)


results = []
for row in lines:
    print('.............Starting new row.......', row)
    solutions = [[1 for i in range(0, 7)] for j in range(0, 7)]
    observations = row[0]
    for word in observations:
        if len(word) == 2:
            solutions = letter_x_can_be_y(solutions, list(word), number_segments[1])
        elif len(word) == 3:
            solutions = letter_x_can_be_y(solutions, list(word), number_segments[7])
        elif len(word) == 4:
            solutions = letter_x_can_be_y(solutions, list(word), number_segments[4])
        elif len(word) == 7:
            solutions = letter_x_can_be_y(solutions, list(word), number_segments[8])
    solutions = check_for_row_pairs(solutions)
    solutions = check_for_singles(solutions)
    solutions = check_for_row_pairs(solutions, [])
    solutions = check_for_singles(solutions)
    # solutions = check_for_row_pairs(solutions, [])
    # solutions = check_for_singles(solutions)
    results.append(make_sense_of_numbers(solutions, row[1]))


print(results)
print('Part 2 is:', sum(results))

# Part 1
# count = 0
# for row in lines:
#     results = row[1]
#     for word in results:
#         if len(word) in [2, 3, 4, 7]:
#             count += 1
#
# print(count)


