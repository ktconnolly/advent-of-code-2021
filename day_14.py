from collections import defaultdict, Counter


def read_input():
    with open("inputs/day_14.txt") as file:
        lines = file.readlines()
        template = lines[0].strip()
        insertions = {}
        for line in lines[2:]:
            p1, p2 = line.strip().split(" -> ")
            insertions[p1] = p2

        return template, insertions


def run_pair_insertion(polymer, instructions, steps):
    char_count = Counter(polymer)
    pair_count = Counter(polymer[i: i + 2] for i in range(len(polymer) - 1))

    for _ in range(steps):
        new_pair_count = defaultdict(int)

        for pair, count in pair_count.items():
            insert = instructions[pair]

            char_count[insert] += count

            new_pair_count[pair[0] + insert] += count
            new_pair_count[insert + pair[1]] += count

        pair_count = new_pair_count

    return max(char_count.values()) - min(char_count.values())


def part_one():
    polymer, instructions = read_input()
    return run_pair_insertion(polymer, instructions, steps=10)


def part_two():
    polymer, instructions = read_input()
    return run_pair_insertion(polymer, instructions, steps=40)


assert part_one() == 2899
assert part_two() == 3528317079545
