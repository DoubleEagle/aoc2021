import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

cave_map = list(map(lambda x: list(map(int, list(x))), open('day15_input.txt').read().split('\n')))

print(np.array(cave_map))

width, height = np.array(cave_map).shape

print(width, height)

# grid = Grid(matrix=cave_map)
#
# start = grid.node(0, 0)
# end = grid.node(width-1, height-1)
#
# finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
# path, runs = finder.find_path(start, end, grid)
#
# # print('operations:', runs, 'path length:', len(path))
# # print(grid.grid_str(path=path, start=start, end=end))
# #
# # print(path)
#
# total_risk = -1 # do not count first step
# for step in path:
#     total_risk += cave_map[step[1]][step[0]]
#
# print('Total risk part 1:', total_risk)

# ---------- Part 2

larger_cave_map = [[0 for i in range(0, width * 5)] for j in range(0, height * 5)]

for i in range(0, 5):
    for row in range(0, width):
        for j in range(0, 5):
            for col in range(0, height):
                current_row = row + i * height
                current_col = col + j * width
                new_value = cave_map[row][col] + i + j if cave_map[row][col] + i + j < 10 else cave_map[row][col] + i + j - 9
                # print(i, ',', row, col, ',', current_row, current_col, ',', cave_map[row][col], new_value)
                # if new_value == 10:
                #     larger_cave_map[current_row][current_col] = 1
                # else:
                larger_cave_map[current_row][current_col] = new_value

print(np.array(larger_cave_map))

grid = Grid(matrix=larger_cave_map)

start = grid.node(0, 0)
end = grid.node(width * 5 - 1, height * 5 - 1)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

print(path)

total_risk = -1 # do not count first step
for step in path:
    total_risk += larger_cave_map[step[1]][step[0]]

print('Total risk part 2:', total_risk)
