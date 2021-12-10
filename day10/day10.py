lines = open('day10_input.txt').read().split('\n')

print(lines)

pairs = [
    ['(', '[', '{', '<'],
    [')', ']', '}', '>']
]

scores_part1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores_part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def detect_corrupt_lines(line):
    to_encounter = ''
    for char in list(line):
        if char in pairs[0]:
            to_encounter += char
        else:
            if to_encounter[-1] != pairs[0][pairs[1].index(char)]:
                # print('panic!!! found', char, 'expected', to_encounter[-1])
                return True, char, to_encounter[-1]
            else:
                to_encounter = to_encounter[:-1]
    return False, None, None


def detect_incomplete_lines(line):
    to_encounter = ''
    for char in list(line):
        if char in pairs[0]:
            to_encounter += char
        else:
            if to_encounter[-1] != pairs[0][pairs[1].index(char)]:
                # print('line is corrupt')
                return ''
            else:
                to_encounter = to_encounter[:-1]

    return ''.join(list(map(lambda x: pairs[1][pairs[0].index(x)], reversed(list(to_encounter)))))


def calc_part2_line_score(completion_string):
    score = 0
    for char in list(completion_string):
        score = score * 5
        score += scores_part2[char]
    return score


part1_scores = 0
for line in lines:
    corrupt, found, expected = detect_corrupt_lines(line)
    if corrupt:
        part1_scores += scores_part1[found]

print('Part 1:', part1_scores)

line_scores = []
for line in lines:
    line_score = 0
    completion_string = detect_incomplete_lines(line)
    if len(completion_string) > 0:
        line_scores.append(calc_part2_line_score(completion_string))

middle_score = sorted(line_scores)[int(len(line_scores)/2)]
print('Part 2:', middle_score)
