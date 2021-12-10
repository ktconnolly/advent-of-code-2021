def read_input():
    with open("inputs/day_10.txt") as file:
        return [line.strip() for line in file]


BRACKET_MAP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",

    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

LEFT_BRACKETS = "([{<"
RIGHT_BRACKETS = ")]}>"

CORRUPTED_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

INCOMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def get_first_illegal_char(s):
    stack = []
    for c in s:
        if c in LEFT_BRACKETS:
            stack.append(c)
        elif c in RIGHT_BRACKETS:
            if stack.pop() != BRACKET_MAP.get(c):
                return c

    return None


def get_required_closing_chars(s):
    stack = []
    for c in s:
        if c in LEFT_BRACKETS:
            stack.append(c)
        elif c in RIGHT_BRACKETS:
            stack.pop()

    return [BRACKET_MAP.get(c) for c in reversed(stack)]


def part_one():
    return sum(CORRUPTED_SCORE.get(get_first_illegal_char(line), 0) for line in read_input())


def part_two():
    incomplete = [line for line in read_input() if get_first_illegal_char(line) is None]
    scores = []
    for line in incomplete:
        score = 0
        for c in get_required_closing_chars(line):
            score = (score * 5) + INCOMPLETE_SCORE.get(c)

        scores.append(score)

    return sorted(scores)[len(scores) // 2]


assert part_one() == 362271
assert part_two() == 1698395182
