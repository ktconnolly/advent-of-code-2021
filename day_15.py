import heapq
from collections import defaultdict

MAX_RISK = 10_000


def read_input():
    with open("inputs/day_15.txt") as file:
        return [list(map(int, list(line.strip()))) for line in file]


def get_all_nodes(height, width):
    for y in range(width):
        for x in range(height):
            yield x, y


def get_neighbours(node, height, width):
    x, y = node

    if y > 0:
        yield x, y - 1
    if y + 1 < height:
        yield x, y + 1
    if x > 0:
        yield x - 1, y
    if x + 1 < width:
        yield x + 1, y


def dijkstra(cave, tiles=1):
    def get_risk(node):
        x, y = node

        if tiles == 1:
            return cave[y][x]

        risk = cave[y % tile_height][x % tile_width] + (y // tile_height) + (x // tile_width)
        return risk % 9 if risk > 9 else risk

    graph = build_graph(cave)

    start = (0, 0)
    pq = [(0, start)]
    heapq.heapify(pq)

    risks = {node: MAX_RISK for node in graph.keys()}
    risks[start] = 0

    height, width = len(cave), len(cave[0])
    tile_height, tile_width = height, width

    if tiles != 1:
        height *= tiles
        width *= tiles

    end = width - 1, height - 1

    while pq:
        current_risk, current_node = heapq.heappop(pq)

        if current_node == end:
            return current_risk

        if current_risk > risks.get(current_node, MAX_RISK):
            continue

        for neighbor in get_neighbours(current_node, height, width):
            neighbour_risk = risks.get(current_node, MAX_RISK) + get_risk(neighbor)

            if neighbour_risk < risks.get(neighbor, MAX_RISK):
                risks[neighbor] = neighbour_risk
                heapq.heappush(pq, (neighbour_risk, neighbor))


def build_graph(cave):
    height, width = len(cave), len(cave[0])
    graph = defaultdict(dict)

    for node in get_all_nodes(height, width):
        for neighbour in get_neighbours(node, height, width):
            n_x, n_y = neighbour
            graph[node][neighbour] = cave[n_y][n_x]

    return graph


def part_one():
    cave = read_input()
    return dijkstra(cave)


def part_two():
    cave = read_input()
    return dijkstra(cave, tiles=5)


assert part_one() == 361
assert part_two() == 2838
