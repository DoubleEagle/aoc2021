input = open('day17_input.txt').read()[13:].split(', ')

target_x = list(map(int, input[0][2:].split('..')))
target_y = list(map(int, input[1][2:].split('..')))


def hits_target(x_velocity, y_velocity):
    position = [0, 0]
    found = False
    max_height = 0
    i = 0
    while not found:
        # update position
        position[0] += x_velocity
        position[1] += y_velocity

        # print(position, x_velocity, y_velocity)

        # update velocities
        if x_velocity != 0:
            x_velocity = x_velocity - 1 if x_velocity > 0 else x_velocity + 1
        # if y_velocity != 0:
        #     y_velocity = y_velocity - 1 if y_velocity > 0 else y_velocity + 1
        y_velocity -= 1

        # check if found
        if target_x[0] <= position[0] <= target_x[1] and target_y[0] <= position[1] <= target_y[1]:
            found = True

        max_height = max(max_height, position[1])

        # break for limiting infinite loop
        i += 1
        if i > 300:
            # print('not found within 100 iterations, breaking...')
            break

    return found, max_height


# print(hits_target(6, 17))



hitting_targets = []
heights = []

for i in range(-300, 300):
    for j in range(-300, 300):
        found, height = hits_target(i, j)
        if found:
            # print('found one!', i, j)
            hitting_targets.append([i, j])
            heights.append(height)


print(hitting_targets[heights.index(max(heights))], max(heights))

print(len(hitting_targets))
