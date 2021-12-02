input_file = open('day2_input.txt')

instructions = input_file.read().split('\n')

def get_position_simple(instructions):
    horizontal = 0
    depth = 0
    for instruction in instructions:
        direction, steps = instruction.split(' ')
        steps = int(steps)
        if direction == 'forward':
            horizontal += steps
        elif direction == 'down':
            depth += steps
        elif direction == 'up':
            depth -= steps
        else:
            print('other instruction, please fix')

    return horizontal, depth


def get_position_with_aim(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        direction, steps = instruction.split(' ')
        steps = int(steps)
        if direction == 'forward':
            horizontal += steps
            depth += steps*aim
        elif direction == 'down':
            aim += steps
        elif direction == 'up':
            aim -= steps
        else:
            print('other instruction, please fix')

    return horizontal, depth


#1
horizontal, depth = get_position_simple(instructions)
print('answer 1: ', horizontal*depth)


#2
horizontal, depth = get_position_with_aim(instructions)
print('answer 2:', horizontal*depth)

