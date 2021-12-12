from collections import defaultdict


def read_input():
    graph = defaultdict(list)
    with open("inputs/day_12.txt") as file:
        for n1, n2 in [line.strip().split("-") for line in file]:
            graph[n1].append(n2)
            graph[n2].append(n1)
    return graph


def count_paths(graph, visited, visit_small_cave_twice, node="start"):
    if node == "end":
        return 1

    count = 0
    for neighbour in graph[node]:
        if neighbour == "start":
            continue

        if neighbour.isupper() or neighbour not in visited:
            count += count_paths(graph, visited + [neighbour], visit_small_cave_twice, neighbour)
        elif visit_small_cave_twice:
            count += count_paths(graph, visited, False, neighbour)

    return count


def part_one():
    cave = read_input()
    return count_paths(cave, visited=[], visit_small_cave_twice=False)


def part_two():
    cave = read_input()
    return count_paths(cave, visited=[], visit_small_cave_twice=True)


assert part_one() == 4970
assert part_two() == 137948
