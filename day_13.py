def read_input():
    with open("inputs/day_13.txt") as file:
        dots = set()
        fold_instructions = []

        for line in file:
            if not line:
                continue

            if line.startswith("fold"):
                axis, value = line.split()[-1].split("=")
                fold_instructions.append((axis, int(value)))
            elif line[0].isdigit():
                x, y = line.split(",")
                dots.add((int(x), int(y)))

        return dots, fold_instructions


def pretty_print(dots):
    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)
    string = ["\n"]

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            if (x, y) in dots:
                row += "#"
            else:
                row += " "

        string.append(row)

    return "\n".join(string)


def fold(dots, fold_instruction):
    axis, value = fold_instruction
    to_remove = set()
    to_add = set()
    for x, y in dots:
        if axis == "y":
            if y > value:
                to_remove.add((x, y))
                to_add.add((x, value - (y - value)))

        elif axis == "x":
            if x > value:
                to_remove.add((x, y))
                to_add.add((value - (x - value), y))

    dots -= to_remove
    dots.update(to_add)


def part_one():
    dots, fold_instructions = read_input()
    fold(dots, fold_instructions[0])
    return len(dots)


def part_two():
    dots, fold_instructions = read_input()
    for instruction in fold_instructions:
        fold(dots, instruction)
    return pretty_print(dots)


assert part_one() == 602
assert part_two() == """

 ##   ##  ####   ## #  # ####  ##  #  #
#  # #  # #       # #  #    # #  # # # 
#    #  # ###     # ####   #  #    ##  
#    #### #       # #  #  #   #    # # 
#  # #  # #    #  # #  # #    #  # # # 
 ##  #  # #     ##  #  # ####  ##  #  #"""
