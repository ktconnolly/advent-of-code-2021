def read_input():
    with open("inputs/day_01.txt") as file:
        return [int(line) for line in file]


def part_one():
    depths = read_input()
    return sum(1 if depths[i] > depths[i - 1] else 0 for i in range(1, len(depths)))


def part_two():
    depths = read_input()

    increase_count = 0
    prev_count = None
    for i in range(len(depths) - 2):
        curr_count = sum(depths[i: i + 3])

        if prev_count is not None and curr_count > prev_count:
            increase_count += 1

        prev_count = curr_count

    return increase_count


assert part_one() == 1301
assert part_two() == 1346
