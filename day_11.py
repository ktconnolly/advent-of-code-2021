def read_input():
    with open("inputs/day_11.txt") as file:
        return [[int(n) for n in line.strip()] for line in file]


def get_neighbours(cavern, x, y):
    points = [(x - 1, y),
              (x + 1, y),
              (x, y - 1),
              (x, y + 1),
              (x - 1, y - 1),
              (x - 1, y + 1),
              (x + 1, y - 1),
              (x + 1, y + 1)]

    return [(x, y) for x, y in points if x in range(len(cavern[0])) and y in range(len(cavern))]


def increment_energy(cavern):
    to_flash = []
    for y in range(len(cavern[0])):
        for x in range(len(cavern)):
            cavern[y][x] += 1
            if cavern[y][x] > 9:
                to_flash.append((x, y))

    return to_flash


def flash(cavern, to_flash):
    to_flash = set(to_flash)
    flashed = set()

    while to_flash:
        (x, y) = to_flash.pop()
        flashed.add((x, y))
        for n in get_neighbours(cavern, x, y):
            if n in flashed:
                continue

            n_x, n_y = n

            cavern[n_y][n_x] += 1
            if cavern[n_y][n_x] > 9:
                to_flash.add(n)

        cavern[y][x] = 0

    return flashed


def step(cavern):
    to_flash = increment_energy(cavern)
    return len(flash(cavern, to_flash))


def part_one():
    cavern = read_input()
    return sum(step(cavern) for _ in range(100))


def part_two():
    cavern = read_input()
    flashed = 0
    count = 0
    total_octopuses = len(cavern[0]) * len(cavern)

    while flashed != total_octopuses:
        flashed = step(cavern)
        count += 1

    return count


assert part_one() == 1681
assert part_two() == 276
