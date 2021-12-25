import copy

import numpy as np

image_enhancement_algorithm, input_image = open('day20_input.txt').read().split('\n\n')

# print(image_enhancement_algorithm)
# print(input_image)

# offset = 100


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print('')
    print('--------------------------------------')


def create_grid(input, offset):
    # input = input.split('\n')
    image_grid = [['.' for i in range(0, len(input[0]) + 2 * offset)] for j in range(0, len(input) + 2 * offset)]

    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] == '#':
                image_grid[row + offset][col + offset] = '#'
    return image_grid


def add_margin(input, cycle_even=True):
    offset = 2
    if cycle_even:
        image_grid = [['.' for i in range(0, len(input[0]) + 2 * offset)] for j in range(0, len(input) + 2 * offset)]
        for row in range(0, len(input)):
            for col in range(0, len(input[0])):
                if input[row][col] == '#':
                    image_grid[row + offset][col + offset] = '#'

    else:
        image_grid = [['#' for i in range(0, len(input[0]) + 2 * offset)] for j in range(0, len(input) + 2 * offset)]
        for row in range(0, len(input)):
            for col in range(0, len(input[0])):
                if input[row][col] == '.':
                    image_grid[row + offset][col + offset] = '.'

    return image_grid


def replace_outer_edge(grid):
    # upper row and lower row
    for col in [0, len(grid) - 1]:
        for row in range(0, len(grid[0])):
            if grid[col][row] == '#':
                grid[col][row] = '.'
            else:
                grid[col][row] = '#'

    # left and right col
    for col in range(1, len(grid) - 1):
        for row in [0, len(grid[0]) - 1]:
            if grid[col][row] == '#':
                grid[col][row] = '.'
            else:
                grid[col][row] = '#'

    return grid



def get_neighbours(row, col, grid):
    width = len(grid[0])
    height = len(grid)
    neighbour_coords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row + i < height and 0 <= col + j < width:
                neighbour_coords.append([row + i, col + j])
    return neighbour_coords


def replace_pixel_value(row, col, old_grid, new_grid, IEA):
    neighbours = get_neighbours(row, col, old_grid)

    # print(neighbours)
    # print_grid()

    if len(neighbours) < 9:
        return new_grid

    binary_string = ''
    for neighbour in neighbours:
        if old_grid[neighbour[0]][neighbour[1]] == '#':
            binary_string = binary_string + '1'
        else:
            binary_string = binary_string + '0'

    new_pixel_value_index = int(binary_string, 2)
    # if new_pixel_value_index == 0:
    #     new_pixel_value_index = 'x'
    new_pixel_value = IEA[new_pixel_value_index]
    # print('new pixel value:', new_pixel_value, IEA, new_pixel_value_index, binary_string)

    new_grid[row][col] = new_pixel_value

    return new_grid


def run_algorithm(grid, IEA):
    new_grid = copy.deepcopy(grid)
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            # print(row, col)
            new_grid = replace_pixel_value(row, col, grid, new_grid, IEA)
            # print('======================= new grid:', row, col)
            # print_grid(new_grid)

    return new_grid


def count_lit_pixels(grid):
    return ''.join(np.array(grid).flatten()).count('#')


offset = 20
grid = create_grid(input_image.split('\n'), 0)
print_grid(grid)
# grid = add_margin(grid)
# print_grid(grid)
# grid = replace_outer_edge(grid)
# print_grid(grid)
# exit()
# print_grid(grid)

cycles = 50
for i in range(0, cycles):
    is_even = True if i % 2 == 0 else False
    # print(i, is_even)
    grid_with_margin = add_margin(grid, is_even)
    # print_grid(grid_with_margin)
    grid = run_algorithm(grid_with_margin, image_enhancement_algorithm)
    # print_grid(grid)
    replace_outer_edge(grid)
    # print_grid(grid)
    # exit()
    # print(grid)
print('')
# print_grid(grid)
# print(len(grid), len(grid[0]))

print('count: ', count_lit_pixels(grid))