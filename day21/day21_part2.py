from cachetools import cached, TTLCache

start_positions = [3, 7]

# global UNIVERSE_COUNTER
# UNIVERSE_COUNTER = 0
wins = [0, 0]

cache = TTLCache(maxsize=100000000000000, ttl=86400)

@cached(cache)
def do_turn(scores, positions, player, total_throw=0, die_number=0):
    scores_new = list(scores)
    positions_new = list(positions)
    wins = (0, 0)

    if die_number == 3:
        positions_new[player] = (positions[player] + total_throw) % 10
        scores_new[player] = scores[player] + positions_new[player] + 1

        if scores_new[player] >= 21:
            wins = [0, 0]
            wins[player] = 1
            return tuple(wins)
        else:
            wins = do_turn(tuple(scores_new), tuple(positions_new), 1 if player == 0 else 0)
    else:
        for throw in range(1, 3+1):
            wins = do_turn(tuple(scores_new), tuple(positions_new), player, total_throw + throw, die_number + 1)

    return wins


result = list(do_turn(tuple([0, 0]), tuple(start_positions), 0))

print(result)


# def roll_dice(scores, positions, player):
#     global UNIVERSE_COUNTER
#     for i in range(1, 4):
#         for j in range(1, 4):
#             for k in range(1, 4):
#                 UNIVERSE_COUNTER += 1
#                 finish_turn(copy.deepcopy(scores), copy.deepcopy(positions), player, i + j + k)


# def finish_turn(scores, positions, player, received_score):
#     if UNIVERSE_COUNTER % 1000000 == 0:
#         print('Universe counter:', UNIVERSE_COUNTER, 'progress:', UNIVERSE_COUNTER // 444356092776315 * 100, '%')
#
#     # update player positions
#     positions[player] = (positions[player] + received_score) % 10
#
#     # update scores
#     scores[player] += positions[player] + 1
#
#     # print('finishing turn, rolled:', received_score, 'scores:', scores, 'positions:', positions, 'universe coutner:', UNIVERSE_COUNTER)
#
#     if scores[player] >= 21:
#         wins[player] += 1
#     else:
#         # update who's turn it is
#         player = 1 if player == 0 else 0
#
#         # initialize next turn
#         roll_dice(copy.deepcopy(scores), copy.deepcopy(positions), player)
#
#
# roll_dice([0, 0], start_positions, 0)

# print(UNIVERSE_COUNTER, wins)