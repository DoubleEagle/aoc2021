import numpy as np

coordinates, instructions = open('day13_input.txt').read().split('\n\n')


coordinates = list(map((lambda x: list(map(int, x.split(',')))), coordinates.split('\n')))

# print(coordinates)
width, height = list(map(lambda x: max(x) + 1, np.transpose(coordinates)))

instructions = list(map(lambda x: [x.split(' ')[2].split('=')[0], int(x.split(' ')[2].split('=')[1])], instructions.split('\n')))

# print(coordinates)
# print(np.max(coordinates))
# print(instructions)

grid = [['.' for i in range(0, width)] for i in range(0, height)]

for x, y in coordinates:
    grid[y][x] = '#'


def draw_sheet(grid):
    for row in grid:
        print(''.join(row))


def get_dimensions_rows_cols(grid):
    draw_sheet(grid)
    return np.array(grid).shape


def do_fold(axis, where, grid):
    # print('folding', axis, where, np.array(grid))
    number_of_rows, number_of_cols = get_dimensions_rows_cols(grid)

    if axis == 'y':
        result = [['.' for i in range(0, number_of_cols)] for i in range(0, number_of_rows//2)]

        for y in range(0, number_of_rows//2):
            for x in range(0, number_of_cols):
                if grid[y][x] == '#' or grid[number_of_rows-y-1][x] == '#':
                    result[y][x] = '#'

    else:
        result = [['.' for i in range(0, number_of_cols//2)] for i in range(0, number_of_rows)]

        for y in range(0, number_of_rows):
            for x in range(0, number_of_cols // 2):
                if grid[y][x] == '#' or grid[y][number_of_cols - 1 - x] == '#':
                    result[y][x] = '#'

    # print('================ result of fold over', axis, 'at', where, 'results are:')
    # draw_sheet(result)
    return result


for instruction in instructions:
    grid = do_fold(instruction[0], instruction[1], grid)

    # for getting part 1
    # print(sum(row.count('#') for row in grid))
    # exit()

draw_sheet(grid)
