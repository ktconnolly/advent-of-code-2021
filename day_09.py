from collections import namedtuple
from functools import reduce

Point = namedtuple("Point", "x y")


def read_input():
    with open("inputs/day_09.txt") as file:
        return [[int(n) for n in list(line.strip())] for line in file]


def get_neighbours(height_map, p):
    h, w = len(height_map), len(height_map[0])

    if p.y > 0:
        yield Point(p.x, p.y - 1)
    if p.y + 1 < h:
        yield Point(p.x, p.y + 1)
    if p.x > 0:
        yield Point(p.x - 1, p.y)
    if p.x + 1 < w:
        yield Point(p.x + 1, p.y)


def is_below_neighbours(height_map, p):
    return all(height_map[p.y][p.x] < height_map[n.y][n.x] for n in get_neighbours(height_map, p))


def get_low_points(height_map):
    def get_all_points():
        h, w = len(height_map), len(height_map[0])
        for y in range(h):
            for x in range(w):
                yield Point(x, y)

    return [p for p in get_all_points() if is_below_neighbours(height_map, p)]


def get_basin(height_map, p):
    basin, found = {p}, set()
    while basin:
        for n in get_neighbours(height_map, basin.pop()):
            if height_map[n.y][n.x] != 9 and n not in found:
                basin.add(n)
                found.add(n)

    return found


def part_one():
    height_map = read_input()
    return sum(height_map[p.y][p.x] + 1 for p in get_low_points(height_map))


def part_two():
    height_map = read_input()
    basin_sizes = [len(get_basin(height_map, p)) for p in get_low_points(height_map)]
    return reduce((lambda x, y: x * y), sorted(basin_sizes)[-3:])


assert part_one() == 522
assert part_two() == 916688
