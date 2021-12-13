def read_input():
    with open("inputs/day_13.txt") as file:
        dots = set()
        fold_instructions = []

        for line in file:
            if line.startswith("fold"):
                axis, value = line.split()[-1].split("=")
                fold_instructions.append((axis, int(value)))
            elif line[0].isdigit():
                x, y = line.split(",")
                dots.add((int(x), int(y)))

        return dots, fold_instructions


def to_string(dots):
    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)
    string = ["\n"]

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += "#" if (x, y) in dots else " "

        string.append(row)

    return "\n".join(string)


def fold(dots, fold_instruction):
    axis, value = fold_instruction
    folded_dots = set()

    for x, y in dots:
        if axis == "y" and y > value:
            y = 2 * value - y
        elif axis == "x" and x > value:
            x = 2 * value - x

        folded_dots.add((x, y))

    return folded_dots


def part_one():
    dots, fold_instructions = read_input()
    dots = fold(dots, fold_instructions[0])
    return len(dots)


def part_two():
    dots, fold_instructions = read_input()
    for instruction in fold_instructions:
        dots = fold(dots, instruction)
    return to_string(dots)


assert part_one() == 602
assert part_two() == """

 ##   ##  ####   ## #  # ####  ##  #  #
#  # #  # #       # #  #    # #  # # # 
#    #  # ###     # ####   #  #    ##  
#    #### #       # #  #  #   #    # # 
#  # #  # #    #  # #  # #    #  # # # 
 ##  #  # #     ##  #  # ####  ##  #  #"""
