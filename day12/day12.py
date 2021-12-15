import copy

import numpy as np

connections = list(map(lambda x: x.split('-'), open('day12_input.txt').read().split('\n')))

cave_connected_to = {cave_name: [] for cave_name in np.unique(connections)}

FOUND_PATHS = []

# make lookup table which connections there are
for cave1, cave2 in connections:
    cave_connected_to[cave1].append(cave2)
    cave_connected_to[cave2].append(cave1)

print(cave_connected_to)


def print_paths(paths):
    for path in paths:
        print(','.join(path))


def can_visit(to_visit, visited):
    found_more_than_once_visited = False
    # large caves may be visited always
    if to_visit.isupper():
        return True
    # if a cave is visited 2 or more times or no times at all, definitely not visiting that one
    if visited.count(to_visit) > 1:
        return False
    if visited.count(to_visit) == 0:
        return True

    # find out if there is cave visited multiple times
    # because of previous clause it will not count itself
    for cave in set(visited):
        if cave.islower():
            if visited.count(cave) > 1:
                return False
    return True


def find_paths(from_cave, walked):
    # print('--------------- called with', from_cave, 'and walked:', walked)
    walked.append(from_cave)
    if from_cave == 'end':
        FOUND_PATHS.append(walked)
    else:
        neighbours = cave_connected_to[from_cave]
        for neighbour in neighbours:
            # print('check', neighbour, walked)
            if neighbour != 'start':
                if can_visit(neighbour, walked):
                    find_paths(neighbour, copy.deepcopy(walked))


print(len(FOUND_PATHS))
