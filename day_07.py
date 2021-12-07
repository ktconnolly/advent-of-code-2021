def read_input():
    with open("inputs/day_07.txt") as file:
        return [int(n) for n in file.readline().split(",")]


def least_fuel(burn_rate):
    crabs = read_input()
    least = None

    for pos in range(min(crabs), max(crabs) + 1):
        total = sum(burn_rate(abs(crab - pos)) for crab in crabs)
        least = total if least is None else min(least, total)

    return least


def part_one():
    return least_fuel(burn_rate=lambda x: x)


def part_two():
    return least_fuel(burn_rate=lambda x: (x * (x + 1)) // 2)


assert part_one() == 344138
assert part_two() == 94862124
