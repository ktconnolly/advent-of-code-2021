def read_input():
    with open("inputs/day_03.txt") as file:
        return [line.strip() for line in file]


def part_one():
    diagnostics = read_input()
    bit_counts = [[0, 0] for _ in range(len(diagnostics[0]))]
    for bits in diagnostics:
        for i, bit in enumerate(bits):
            if bit == "0":
                bit_counts[i][0] += 1
            else:
                bit_counts[i][1] += 1

    gamma, epsilon = "", ""
    for zero_count, one_count in bit_counts:
        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


assert part_one() == 4138664
