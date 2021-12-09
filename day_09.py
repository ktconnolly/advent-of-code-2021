from collections import namedtuple
from functools import reduce

Point = namedtuple("Point", "x y")


def read_input():
    with open("inputs/day_09.txt") as file:
        return [[int(n) for n in list(line.strip())] for line in file]


def get_neighbours(height_map, p):
    neighbours = Point(p.x + 1, p.y), Point(p.x - 1, p.y), Point(p.x, p.y + 1), Point(p.x, p.y - 1)
    h, w = len(height_map), len(height_map[0])
    return [n for n in neighbours if n.y in range(h) and n.x in range(w)]


def is_below_neighbours(height_map, p):
    return all(height_map[p.y][p.x] < height_map[n.y][n.x] for n in get_neighbours(height_map, p))


def get_low_points(height_map):
    h, w = len(height_map), len(height_map[0])
    return [Point(x, y) for y in range(h) for x in range(w) if is_below_neighbours(height_map, Point(x, y))]


def get_basin(height_map, p):
    neighbours = get_neighbours(height_map, p)

    basin, searched = {p}, {p}
    while neighbours:
        n = neighbours.pop()
        searched.add(n)

        if height_map[n.y][n.x] != 9:
            basin.add(n)
            neighbours += [n for n in get_neighbours(height_map, n) if n not in searched]

    return basin


def part_one():
    height_map = read_input()
    return sum(height_map[p.y][p.x] + 1 for p in get_low_points(height_map))


def part_two():
    height_map = read_input()
    basin_sizes = [len(get_basin(height_map, p)) for p in get_low_points(height_map)]
    return reduce((lambda x, y: x * y), sorted(basin_sizes)[-3:])


assert part_one() == 522
assert part_two() == 916688
