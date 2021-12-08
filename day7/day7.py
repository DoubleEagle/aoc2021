numbers = list(map(int, open('day7_dummyinput.txt').read().split(',')))

print(numbers)


def calc_total_fuel(numbers, position):
    distances = list(map(lambda num: (abs(num - position)*(abs(num - position)+1))/2, numbers))
    return sum(distances)


results = []
results_i = []
for i in range(min(numbers), max(numbers)):
    results.append(calc_total_fuel(numbers, i))
    results_i.append(i)

print(min(results))
# print(results_i[results.index(min(results))])
