from collections import Counter


def read_input():
    with open("inputs/day_03.txt") as file:
        return [line.strip() for line in file]


def part_one():
    gamma, epsilon = "", ""
    for col_count in [Counter(col) for col in (zip(*read_input()))]:
        if col_count["0"] > col_count["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def get_rating(diagnostics, oxygen):
    col = 0
    while len(diagnostics) != 1:
        col_count = Counter(list(zip(*diagnostics))[col])

        if oxygen:
            bit_to_keep = "0" if col_count["0"] > col_count["1"] else "1"
        else:
            bit_to_keep = "1" if col_count["0"] > col_count["1"] else "0"

        diagnostics = [bits for bits in diagnostics if bits[col] == bit_to_keep]
        col += 1

    return int(diagnostics[0], 2)


def part_two():
    diagnostics = read_input()
    return get_rating(diagnostics, oxygen=True) * get_rating(diagnostics, oxygen=False)


assert part_one() == 4138664
assert part_two() == 4273224
