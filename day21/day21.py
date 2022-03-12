player_positions = [7, 1]
scores = [0, 0]


turn_counter = 0
whos_turn_is_it_anyways = 0


while scores[0] < 1000 and scores[1] < 1000:
    # roll die
    rolled = 0
    for i in range(turn_counter * 3 + 1, turn_counter * 3 + 1 + 3):
        print(i)
        rolled += i

    # update player position
    player_positions[whos_turn_is_it_anyways] = (player_positions[whos_turn_is_it_anyways] + rolled) % 10

    # update score
    scores[whos_turn_is_it_anyways] += player_positions[whos_turn_is_it_anyways] + 1

    print("Turn number:", turn_counter, "It's Player", whos_turn_is_it_anyways, "'s turn", rolled, 'positions are:', player_positions, 'scored are:', scores)
    # update who's turn it is
    whos_turn_is_it_anyways = 1 if whos_turn_is_it_anyways == 0 else 0

    # update turn counter
    turn_counter += 1

print(scores, turn_counter * 3, min(scores) * turn_counter * 3)