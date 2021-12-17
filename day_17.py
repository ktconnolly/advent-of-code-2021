import re
from collections import namedtuple

Target = namedtuple("Target", "min_x max_x min_y max_y")


def read_input():
    with open("inputs/day_17.txt") as file:
        line = file.readline().strip()
        (x_min, x_max), (y_min, y_max) = re.findall("=(-?\d*)..(-?\d*)", line)
        return Target(int(x_min), int(x_max), int(y_min), int(y_max))


def step(pos, velocity):
    x, y = pos
    dx, dy = velocity

    x += dx
    y += dy

    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1

    dy -= 1

    return (x, y), (dx, dy)


def in_target(pos, target):
    x, y = pos
    return target.min_x <= x <= target.max_x and target.min_y <= y <= target.max_y


def launch_probe(target, velocity, pos=(0, 0)):
    path = []

    while not in_target(pos, target):
        pos, velocity = step(pos, velocity)

        x, y = pos
        if x > target.max_x or y < target.min_y:
            return []

        path.append(pos)

    return path


def get_paths(target):
    for y in range(target.min_y, max(abs(target.min_y), abs(target.max_y))):
        for x in range(target.max_x + 1):
            path = launch_probe(target, velocity=(x, y))
            if path:
                yield path


def part_one():
    target = read_input()
    return max(max(y for _, y in p) for p in get_paths(target))


def part_two():
    target = read_input()
    return sum(1 for p in get_paths(target) if p)


assert part_one() == 3003
assert part_two() == 940
