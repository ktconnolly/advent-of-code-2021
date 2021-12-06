def read_input():
    with open("inputs/day_06.txt") as file:
        return [int(n) for n in file.readline().split(",")]


def spawn(days):
    age_counts = [0] * 9
    for age in read_input():
        age_counts[age] += 1

    for i in range(days):
        age_counts[(i + 7) % 9] += age_counts[i % 9]

    return sum(age_counts)


def part_one():
    return spawn(days=80)


def part_two():
    return spawn(days=256)


assert part_one() == 372300
assert part_two() == 1675781200288
