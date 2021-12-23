from collections import namedtuple
from functools import lru_cache
from itertools import product

Player = namedtuple("player", "space score")


def read_input():
    with open("inputs/day_21.txt") as file:
        return [Player(space=int(line.split()[-1]), score=0) for line in file]


class Die:
    def __init__(self):
        self.value = 1
        self.roll_count = 0

    def roll(self):
        self.roll_count += 1
        value = self.value
        self.value += 1
        if self.value == 101:
            self.value = 1
        return value


def move(player, spaces):
    new_space = player.space + spaces
    score = player.score

    if new_space == 10 or new_space % 10 == 0:
        new_space = 10
        score += 10
    else:
        new_space = new_space % 10
        score += new_space

    return Player(new_space, score)


QUANTUM_ROLLS = [sum(roll) for roll in product(range(1, 4), repeat=3)]


def part_one():
    p1, p2 = read_input()

    die = Die()

    p1_turn = True
    while True:
        if p1.score >= 1000:
            return p2.score * die.roll_count
        if p2.score >= 1000:
            return p1.score * die.roll_count

        roll = die.roll() + die.roll() + die.roll()

        if p1_turn:
            p1 = move(p1, roll)
        else:
            p2 = move(p2, roll)

        p1_turn = not p1_turn


@lru_cache(maxsize=None)
def quantum_play(p1, p2, roll, p1_turn=True):
    if p1_turn:
        p1 = move(p1, roll)
    else:
        p2 = move(p2, roll)

    if p1.score >= 21:
        return 1, 0
    if p2.score >= 21:
        return 0, 1

    p1_total_wins = 0
    p2_total_wins = 0

    for roll in QUANTUM_ROLLS:
        p1_wins, p2_wins = quantum_play(p1, p2, roll, not p1_turn)
        p1_total_wins += p1_wins
        p2_total_wins += p2_wins

    return p1_total_wins, p2_total_wins


def part_two():
    player_1, player_2 = read_input()

    p1_total_wins = 0
    p2_total_wins = 0

    for roll in QUANTUM_ROLLS:
        p1_wins, p2_wins = quantum_play(player_1, player_2, roll)
        p1_total_wins += p1_wins
        p2_total_wins += p2_wins

    return max(p1_total_wins, p2_total_wins)


assert part_one() == 855624
assert part_two() == 187451244607486
