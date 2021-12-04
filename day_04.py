from collections import OrderedDict


def read_input():
    with open("inputs/day_04.txt") as file:
        numbers, *boards = [entry.strip() for entry in file.read().split("\n\n")]
        numbers = [int(n) for n in numbers.split(",")]
        boards = [[[int(n) for n in row.split()] for row in board.splitlines()] for board in boards]
        return numbers, boards


class BingoGame:
    def __init__(self, numbers, boards):
        self.numbers = numbers
        self.boards = boards
        self.called_numbers = []
        # key is board index, value is score at time of winning
        self.winning_scores = OrderedDict()

    def call_number(self):
        number = self.numbers.pop(0)
        self.called_numbers.append(number)
        self.populate_scores()

    def populate_scores(self):
        for i, board in enumerate(self.boards):
            if i not in self.winning_scores and self.is_winner(board):
                self.winning_scores[i] = self.get_score(board)

    def get_score(self, board):
        return self.get_unmarked_sum(board) * self.called_numbers[-1]

    def is_winner(self, board):
        return self.has_complete_column(board) or self.has_complete_row(board)

    def has_complete_column(self, board):
        return any(not self.get_unmarked_numbers(col) for col in zip(*board))

    def has_complete_row(self, board):
        return any(not self.get_unmarked_numbers(row) for row in board)

    def get_unmarked_sum(self, board):
        return sum(sum(self.get_unmarked_numbers(row)) for row in board)

    def get_unmarked_numbers(self, numbers):
        return set(numbers).difference(self.called_numbers)


def get_bingo_game():
    numbers, boards = read_input()
    return BingoGame(numbers, boards)


def part_one():
    bingo = get_bingo_game()

    while not bingo.winning_scores:
        bingo.call_number()

    _, score = bingo.winning_scores.popitem()
    return score


def part_two():
    bingo = get_bingo_game()

    while len(bingo.boards) != len(bingo.winning_scores):
        bingo.call_number()

    last_winner = next(reversed(bingo.winning_scores))
    return bingo.winning_scores[last_winner]


assert part_one() == 8136
assert part_two() == 12738
