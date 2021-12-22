from itertools import combinations

# first list is element order, second is signs to apply to elements
# eg. [2, 0, 1] will convert [x, y, z] to [z, x, y]
# [-1, -1, 1] will convert  [x, y, z] to [-x, -y, z]
# combined this will give [z, -x, -y]
ROTATIONS = [
    ([2, 0, 1], [-1, -1, 1]),
    ([0, 1, 2], [1, -1, -1]),
    ([2, 1, 0], [-1, -1, -1]),
    ([2, 1, 0], [1, -1, 1]),
    ([0, 2, 1], [-1, -1, -1]),
    ([1, 2, 0], [1, -1, -1]),
    ([1, 0, 2], [-1, -1, -1]),
    ([1, 2, 0], [1, 1, 1]),
    ([0, 2, 1], [-1, 1, 1]),
    ([0, 1, 2], [-1, 1, -1]),
    ([0, 2, 1], [1, -1, 1]),
    ([2, 0, 1], [-1, 1, -1]),
    ([1, 0, 2], [1, 1, -1]),
    ([2, 1, 0], [1, 1, -1]),
    ([2, 0, 1], [1, 1, 1]),
    ([2, 1, 0], [-1, 1, 1]),
    ([0, 1, 2], [1, 1, 1]),
    ([1, 0, 2], [1, -1, 1]),
    ([1, 0, 2], [-1, 1, 1]),
    ([0, 1, 2], [-1, -1, 1]),
    ([1, 2, 0], [-1, 1, -1]),
    ([1, 2, 0], [-1, -1, 1]),
    ([0, 2, 1], [1, 1, -1]),
    ([2, 0, 1], [1, -1, -1])
]


def read_input():
    with open("inputs/day_19.txt") as file:
        scanners = []
        for i, s in enumerate([scanner for scanner in file.read().split("\n\n")]):
            beacons = set(tuple(int(b) for b in line.strip().split(",")) for line in s.splitlines()[1:])
            scanners.append(beacons)

        return scanners


def rotate(beacon, rotation):
    orders, signs = rotation
    coords = [b * s for b, s in zip(beacon, signs)]
    return [coords[orders[i]] for i in range(3)]


def rotate_scanner(scanner):
    for rotation in ROTATIONS:
        yield [rotate(beacon, rotation) for beacon in scanner]


def get_distance(b1, b2):
    return abs(b1[0] - b2[0]) + abs(b1[1] - b2[1]) + abs(b1[2] - b2[2])


def adjust(beacon, offset):
    return beacon[0] + offset[0], beacon[1] + offset[1], beacon[2] + offset[2]


def get_adjusted_beacons(reference_scanner, scanner):
    for rotation in rotate_scanner(scanner):
        for rotated_beacon in rotation:
            for reference_beacon in reference_scanner:
                offset = (reference_beacon[0] - rotated_beacon[0],
                          reference_beacon[1] - rotated_beacon[1],
                          reference_beacon[2] - rotated_beacon[2])

                adjusted_scanner = set(adjust(beacon, offset) for beacon in rotation)
                if len(adjusted_scanner.intersection(reference_scanner)) > 11:
                    return adjusted_scanner, offset

    return None, None


def get_beacons():
    scanners = read_input()
    reference = scanners[0]
    unaligned = [i for i in range(1, len(scanners))]
    offsets = {0: (0, 0, 0)}

    while unaligned:
        for i in unaligned:
            beacons, offset = get_adjusted_beacons(reference, scanners[i])
            if beacons is not None:
                unaligned.remove(i)
                offsets[i] = offset
                reference.update(beacons)

    return reference, offsets


def get_manhattan_distance(o1, o2):
    return abs(o1[0] - o2[0]) + abs(o1[1] - o2[1]) + abs(o1[2] - o2[2])


def get_max_distance(offsets):
    return max(get_manhattan_distance(o1, o2) for o1, o2 in combinations(offsets, 2))


beacons, offsets = get_beacons()

# part 1
assert len(beacons) == 394
# part 2
assert get_max_distance([i for i in offsets.values()]) == 12304
