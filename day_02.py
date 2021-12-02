def read_input():
    with open("inputs/day_02.txt") as file:
        return [line.strip().split(" ") for line in file]


def part_one():
    depth, horizontal = 0, 0

    for direction, distance in read_input():
        if direction == "forward":
            horizontal += int(distance)
        elif direction == "down":
            depth += int(distance)
        elif direction == "up":
            depth -= int(distance)

    return depth * horizontal


def part_two():
    depth, horizontal, aim = 0, 0, 0

    for direction, distance in read_input():
        if direction == "forward":
            horizontal += int(distance)
            depth += aim * int(distance)
        elif direction == "down":
            aim += int(distance)
        elif direction == "up":
            aim -= int(distance)

    return depth * horizontal


assert part_one() == 2027977
assert part_two() == 1903644897
