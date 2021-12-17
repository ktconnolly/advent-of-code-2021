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


def launch_probe(velocity, target, pos=(0, 0)):
    path = []

    while not in_target(pos, target):
        pos, velocity = step(pos, velocity)

        x, y = pos
        if x > target.max_x or y < target.min_y:
            return False, path

        path.append(pos)

    return True, path


def get_max_heights(target):
    heights = []
    for y in range(target.min_y, max(abs(target.min_y), abs(target.max_y))):
        for x in range(target.max_x + 1):
            velocity = x, y
            hit_target, path = launch_probe(velocity, target)

            if hit_target:
                heights.append(max(y for _, y in path))

    return heights


def part_one():
    target = read_input()
    return max(get_max_heights(target))


def part_two():
    target = read_input()
    return len(get_max_heights(target))


assert part_one() == 3003
assert part_two() == 940
