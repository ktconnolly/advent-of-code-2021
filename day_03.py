def read_input():
    with open("inputs/day_03.txt") as file:
        return [line.strip() for line in file]


def get_bit_counts(diagnostics):
    bit_counts = [[0, 0] for _ in range(len(diagnostics[0]))]
    for bits in diagnostics:
        for i, bit in enumerate(bits):
            if bit == "0":
                bit_counts[i][0] += 1
            else:
                bit_counts[i][1] += 1

    return bit_counts


def get_bit_counts_for_index(diagnostics, index):
    bit_counts = [0, 0]
    for bits in diagnostics:
        if bits[index] == "0":
            bit_counts[0] += 1
        else:
            bit_counts[1] += 1

    return bit_counts


def get_rating(diagnostics, oxygen):
    i = 0
    while len(diagnostics) != 1:
        zero_count, one_count = get_bit_counts_for_index(diagnostics, index=i)

        if oxygen:
            bit_to_keep = "0" if zero_count > one_count else "1"
        else:
            bit_to_keep = "1" if zero_count > one_count else "0"

        diagnostics = [bits for bits in diagnostics if bits[i] == bit_to_keep]
        i += 1

    return int(diagnostics[0], 2)


def part_one():
    diagnostics = read_input()

    gamma, epsilon = "", ""
    for zero_count, one_count in get_bit_counts(diagnostics):
        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def part_two():
    diagnostics = read_input()
    return get_rating(diagnostics, oxygen=True) * get_rating(diagnostics, oxygen=False)


assert part_one() == 4138664
assert part_two() == 4273224
