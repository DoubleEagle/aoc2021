import math

import numpy as np

map_ocean = list(map(lambda x: list(map(int, list(x))), open('day9_input.txt').read().split('\n')))

ROWS_COUNT, COLS_COUNT = np.array(map_ocean).shape
# print(np.array(map))


def get_neighbours_without_9s(point):
    # yep this could do better as well
    found = []
    row = point[0]
    col = point[1]
    if row != 0 and map_ocean[row - 1][col] != 9:
        # print('found north')
        found.append((row - 1, col))
    if row != ROWS_COUNT - 1 and map_ocean[row + 1][col] != 9:
        # print('found south')
        found.append((row + 1, col))
    if col != 0 and map_ocean[row][col - 1] != 9:
        # print('found west')
        found.append((row, col - 1))
    if col != COLS_COUNT - 1 and map_ocean[row][col + 1] != 9:
        # print('found east')
        found.append((row, col + 1))
    return found


def get_unchecked_neighbours_count(point, checked):
    # count and check itself
    count = 1
    checked.append(point)

    neighbours = get_neighbours_without_9s(point)

    for neighbour in neighbours:
        if neighbour not in checked:
            tmpcount, checked = get_unchecked_neighbours_count(neighbour, checked)
            count += tmpcount

    return count, checked


low_points_coordinates = []

for row in range(0, ROWS_COUNT):
    for col in range(0, COLS_COUNT):
        # could probably do this better with the get_neighbours shizzle, but too tired to do anything about it
        if row != 0 and map_ocean[row][col] >= map_ocean[row - 1][col]:
            continue
        if row != ROWS_COUNT - 1 and map_ocean[row][col] >= map_ocean[row + 1][col]:
            continue
        if col != 0 and map_ocean[row][col] >= map_ocean[row][col - 1]:
            continue
        if col != COLS_COUNT - 1 and map_ocean[row][col] >= map_ocean[row][col + 1]:
            continue
        low_points_coordinates.append((row, col))

# print(low_points_coordinates)
print('Answer part 1:', sum(list(map(lambda x: map_ocean[x[0]][x[1]] + 1, low_points_coordinates))))

results = []

for coord in low_points_coordinates:
    count, checked = get_unchecked_neighbours_count(coord, [])
    results.append(count)

# print(results)

top3 = sorted(results, reverse=True)[:3]
product = np.prod(top3)
print('Answer part 2:', product)
