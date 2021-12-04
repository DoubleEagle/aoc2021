import copy

import numpy as np

input_file = open('day4_input.txt')

objects = input_file.read().split('\n\n')

drawn = list(map(lambda x: int(x), objects[0].split(',')))
# Please excuse my unreadable code, I'm just starting to learn about map functions etc, and I'm
# thoroughly enjoying myself.
boards = list(
    map(lambda board: list(map(lambda row: list(map(int, list(filter(len, row.split(' '))))), board.split('\n'))),
        objects[1:]))
called = list(map(lambda board: [[0] * 5 for i in range(5)], boards))


def check_which_boards_win(called):
    winning_boards = []
    for board_no in range(0, len(called)):
        a = np.array(called[board_no])
        if check_if_horizontal(called, board_no) or check_if_vertical(called, board_no):
            winning_boards.append(board_no)
    return winning_boards


def check_if_vertical(called, board_no):
    a = np.array(called[board_no])
    a = a.transpose()
    for row in a:
        if np.count_nonzero(row) == 5:
            return True
    return False


def check_if_horizontal(called, board_no):
    a = np.array(called[board_no])
    for row in a:
        if np.count_nonzero(row) == 5:
            return True
    return False


def call_number(boards, called, number):
    for board_no in range(0, len(called)):
        for row_no in range(0, len(called[board_no])):
            for col_no in range(0, len(called[board_no][row_no])):
                if boards[board_no][row_no][col_no] == number:
                    print('Called number', number, 'at', board_no, row_no, col_no)
                    called[board_no][row_no][col_no] = 1
    return called


def sum_winning_board(boards, board_no, called):
    sum = 0
    for row_no in range(0, len(called)):
        for col_no in range(0, len(called[row_no])):
            if called[row_no][col_no] != 1:
                sum += boards[board_no][row_no][col_no]
    return sum


boards_that_won = []
winning_numbers = []
winning_board_call_cards = []

for number in drawn:
    called = call_number(boards, called, number)
    winning_boards = check_which_boards_win(called)
    for b in winning_boards:
        if not (b in boards_that_won):
            boards_that_won.append(b)
            winning_numbers.append(number)
            winning_board_call_cards.append(copy.deepcopy(called[b]))

print('Part 1 answer:', sum_winning_board(boards, boards_that_won[0], winning_board_call_cards[0]) * winning_numbers[0])
print('Part 2 answer:', sum_winning_board(boards, boards_that_won[-1], winning_board_call_cards[-1]) * winning_numbers[-1])
