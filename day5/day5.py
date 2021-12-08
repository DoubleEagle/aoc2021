import numpy as np

inputfile = open('day5_input.txt')

lines = list(map(lambda x: x.split(' -> '), inputfile.read().split('\n')))

lines = list(map(lambda x: [list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))], lines))

# lines = list(map(lambda x: [[x[0][0] - 1, x[0][1] - 1], [x[1][0] - 1, x[1][1] - 1]], lines))

max_width_height = np.amax(lines) + 1

grid = [ [ 0 for y in range( max_width_height ) ] for x in range( max_width_height ) ]


def add_to_x_y(grid, x, y):
    grid[y][x] += 1
    return grid


def add_diagonal(grid, x_start, y_start, x_end, y_end):
    print('fixing that diagonal')

    if y_start < y_end:
        print('line is ascending y')
        coefficient_y = 1
        y_end += 1
    else:
        print('line is descending y')
        coefficient_y = -1
        y_end -= 1
    if x_start < x_end:
        print('line is ascending')
        coefficient_x = 1
        x_end += 1
    else:
        print('line is descending')
        coefficient_x = -1
        x_end -= 1
    x_list = list(range(x_start, x_end, coefficient_x))
    y_list = list(range(y_start, y_end, coefficient_y))

    for i in range(0, len(x_list)):
        grid = add_to_x_y(grid, x_list[i], y_list[i])
    
    return grid


def draw_line(grid, x_start, y_start, x_end, y_end):
    # a = np.array(grid)
    # print(a, x_start, y_start, x_end, y_end)
    if x_start == x_end:
        print('vertical detected', x_start, y_start, x_end, y_end)
        if y_start < y_end:
            for i in range(y_start, y_end + 1):
                grid = add_to_x_y(grid, x_start, i)
        else:
            for i in range(y_end, y_start + 1):
                grid = add_to_x_y(grid, x_start, i)
        # print(np.array(grid))
    elif y_start == y_end:
        print('horizontal detected', x_start, y_start, x_end, y_end)
        if x_start < x_end:
            for i in range(x_start, x_end + 1):
                grid = add_to_x_y(grid, i, y_start)
        else:
            for i in range(x_end, x_start + 1):
                grid = add_to_x_y(grid, i, y_start)
        # print(np.array(grid))
    else:
        print('/// diagonal detected!', x_start, y_start, x_end, y_end)
        add_diagonal(grid, x_start, y_start, x_end, y_end)
          
    return grid


for line in lines:
    grid = draw_line(grid, line[0][0], line[0][1], line[1][0], line[1][1])

print(np.array(grid))
print(np.count_nonzero(np.array(grid) > 1))
