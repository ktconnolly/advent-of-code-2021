import re
from collections import namedtuple, defaultdict

Point = namedtuple("Point", "x y")


def read_input():
    with open("inputs/day_05.txt") as file:
        return [[Point(int(x1), int(y1)), Point(int(x2), int(y2))] for (x1, y1), (x2, y2) in
                [re.findall(r'(\d*),(\d*)', line) for line in file]]


def get_points_between(p1, p2):
    def sign(x, y):
        return (x > y) - (x < y)

    (x1, y1), (x2, y2) = p1, p2

    yield Point(x1, y1)

    dx = sign(x2, x1)
    dy = sign(y2, y1)

    while x1 != x2 or y1 != y2:
        x1 += dx
        y1 += dy
        yield Point(x1, y1)


def get_intersection_count(include_diagonals):
    intersection_sums = defaultdict(int)
    for p1, p2 in read_input():
        if include_diagonals or (p1.x == p2.x or p1.y == p2.y):
            for p in get_points_between(p1, p2):
                intersection_sums[p] += 1

    return sum(1 if intersections > 1 else 0 for intersections in intersection_sums.values())


def part_one():
    return get_intersection_count(include_diagonals=False)


def part_two():
    return get_intersection_count(include_diagonals=True)


assert part_one() == 5632
assert part_two() == 22213
