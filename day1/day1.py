input_file = open('day1_input.txt')

numbers = input_file.read().split('\n')

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])


def count_increase_decrease_same(numbers):
    num_increase = 0
    num_decrease = 0
    num_same = 0

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] > 0:
            print('increase')
            num_increase += 1
        elif numbers[i] - numbers[i-1] < 0:
            print('decrease')
            num_decrease += 1
        else:
            print('same')
            num_same += 1

    return num_increase, num_decrease, num_same


def sliding_window_increased(numbers):
    increased = 0
    prev_sum = 0

    for i in range(2, len(numbers)):
        sum = numbers[i-2] + numbers[i-1] + numbers[i]
        if i != 2 and sum > prev_sum:
            increased += 1
        prev_sum = sum

    return increased


print(sliding_window_increased(numbers))