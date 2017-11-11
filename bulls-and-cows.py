from random import choice, sample
from itertools import permutations

# common
def score(x, y):
    bulls = sum(i == j for i, j in zip(x, y))
    cows = len(set(x) & set(y)) - bulls
    return bulls, cows

# player 1
def player1(player2):
    secret = sample(range(10), 4)

    tip = next(player2)
    while True:
        b, c = score(secret, tip)
        if b < 4:
            print(b, 'bulls', c, 'cows')
            tip = player2.send((b, c))
        else:
            print('you won')
            break

# player 2
def player2():
    tips = list(permutations(range(10), 4))

    while True:
        tip = choice(tips)
        print(tip, '?')
        bc = yield tip
        tips = [i for i in tips if score(i, tip) == bc]

# game
player1(player2())
player1(player2())
