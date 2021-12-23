def read_input():
    with open("inputs/day_20.txt") as file:
        algorithm, image = file.read().split("\n\n")
        return algorithm, image.split()


def get_neighbours(x, y):
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def enhance(algorithm, image, iteration):
    height = len(image)
    width = len(image[0])

    if algorithm[0] == "#" and algorithm[-1] == ".":
        background = "#" if iteration % 2 == 0 else "."
    else:
        background = "."

    output = [[background for _ in range(width)] for _ in range(height)]

    for y in range(height - 1):
        for x in range(width - 1):
            pixels = [image[y][x] for x, y in get_neighbours(x, y)]
            binary = ["1" if p == "#" else "0" for p in pixels]
            output[y][x] = algorithm[int("".join(binary), 2)]

    return output


def pad_image(image, amount):
    height = len(image)
    width = len(image[0])

    padded = [["." for _ in range(width + 2 * amount)] for _ in range(height + 2 * amount)]

    for y in range(height):
        for x in range(width):
            padded[y + amount][x + amount] = image[y][x]

    return padded


def get_pixel_count(algorithm, image, iterations):
    image = pad_image(image, amount=iterations + 1)

    for i in range(iterations):
        image = enhance(algorithm, image, i)

    return sum(col == "#" for row in image for col in row)


def part_one():
    algorithm, image = read_input()
    return get_pixel_count(algorithm, image, iterations=2)


def part_two():
    algorithm, image = read_input()
    return get_pixel_count(algorithm, image, iterations=50)


assert part_one() == 5663
assert part_two() == 19638
