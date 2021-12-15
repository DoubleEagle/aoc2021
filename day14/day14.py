import copy

import numpy as np

start_string, pair_insertion_rules = open('day14_input.txt').read().split('\n\n')

pair_insertion_rules_list = list(map(lambda x: x.split(' -> '), pair_insertion_rules.split('\n')))

pair_insertion_rules = dict()

for bigram, insert in pair_insertion_rules_list:
    pair_insertion_rules[bigram] = insert

print(start_string, pair_insertion_rules)

bigrams = dict()

# throw string in buckets
start_string_bigrams = [start_string[i:i + 2] for i in range(len(start_string) - 1)]

for bigram in start_string_bigrams:
    if bigram in bigrams:
        bigrams[bigram] += 1
    else:
        bigrams[bigram] = 1


letter_frequencies = dict()

for letter in list(start_string):
    if letter in letter_frequencies:
        letter_frequencies[letter] += 1
    else:
        letter_frequencies[letter] = 1


def do_step(bigrams):
    bigrams_ref = copy.deepcopy(bigrams)

    for bigram in bigrams_ref:
        # print(' should be the same!', bigrams_ref)
        if bigrams_ref[bigram] > 0 and bigram in pair_insertion_rules:
            left_new_bigram = bigram[0] + pair_insertion_rules[bigram]
            right_new_bigram = pair_insertion_rules[bigram] + bigram[1]
            # print('inserted', left_new_bigram, 'and', right_new_bigram, 'and removed', bigram, 'new letter is', pair_insertion_rules[bigram])
            how_many_bigrams_affected = bigrams_ref[bigram]
            if left_new_bigram in bigrams:
                bigrams[left_new_bigram] += how_many_bigrams_affected
            else:
                bigrams[left_new_bigram] = how_many_bigrams_affected

            if right_new_bigram in bigrams:
                bigrams[right_new_bigram] += how_many_bigrams_affected
            else:
                bigrams[right_new_bigram] = how_many_bigrams_affected

            if pair_insertion_rules[bigram] in letter_frequencies:
                letter_frequencies[pair_insertion_rules[bigram]] += how_many_bigrams_affected
            else:
                letter_frequencies[pair_insertion_rules[bigram]] = how_many_bigrams_affected

            bigrams[bigram] -= how_many_bigrams_affected

            print('===== debugging info')
            print(bigram, '--- inserted', left_new_bigram, 'and', right_new_bigram, 'new letter is',
                  pair_insertion_rules[bigram], 'no of bigrams affected:', bigrams_ref[bigram])
            print('\t', bigrams)
            print('\t', letter_frequencies)
    # print(' should be the same! 2', bigrams_ref)

    return bigrams


for i in range(0, 40):
    print('========================================== STEP', i)
    print(bigrams)
    print(letter_frequencies)
    bigrams = do_step(bigrams)

print(letter_frequencies)
print(max(letter_frequencies.values())-min(letter_frequencies.values()))