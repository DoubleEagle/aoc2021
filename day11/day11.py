import numpy as np

GRID = list(map(lambda line: list(map(int, list(line))), open('day11_input.txt').read().split('\n')))

print('Input:', np.array(GRID))


def get_neighbours(grid, point):
    neighbours = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (0 <= point[0] + r < len(grid)) and (0 <= point[1] + c < len(grid)):
                neighbours.append((point[0] + r, point[1] + c))
    return neighbours


def do_flash(grid):
    flashed_cells = []
    # light up neighbours
    while any(max(row) > 9 for row in grid):
        # find 9's
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] > 9:
                    # print('flash at row/col', row, col)
                    neighbours = get_neighbours(grid, (row, col))
                    for neighbour in neighbours:
                        grid[neighbour[0]][neighbour[1]] += 1
                    flashed_cells.append((row, col))
        for row, col in flashed_cells:
            grid[row][col] = 0
    return grid, len(flashed_cells)


def do_tick(grid):
    # increase all cells by 1
    grid = list(map(lambda line: list(map(lambda x: x+1, line)), grid))

    # do flash
    grid, count = do_flash(grid)

    return grid, count


result_1 = 0
for i in range(0, 1000):

    print('Step number...', i + 1)
    GRID, count = do_tick(GRID)
    result_1 += count
    if i == 99:
        print('part 1:', result_1)
        # exit()

    # part 2
    print('sum of grid:', np.sum(GRID))
    if np.sum(GRID) == 0:
        print('flashed all at the same time at step', i, ':O')
        exit()
