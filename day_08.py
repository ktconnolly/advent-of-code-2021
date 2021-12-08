from utils import *


def read_input():
    with open("inputs/day_08.txt") as file:
        return [(l1.split(), l2.split()) for l1, l2 in [l.strip().split(" | ") for l in file.readlines()]]


def part_one():
    return sum(len(digit) in (2, 3, 4, 7) for digit in flatten([output for _, output in read_input()]))


def get_numbers_map(signals):
    numbers = {}
    five_len = []
    six_len = []

    for s in signals:
        if len(s) == 2:
            numbers[1] = s
        elif len(s) == 7:
            numbers[8] = s
        elif len(s) == 3:
            numbers[7] = s
        elif len(s) == 4:
            numbers[4] = s
        elif len(s) == 5:
            five_len.append(s)
        elif len(s) == 6:
            six_len.append(s)

    for s in six_len:
        if set(numbers[4]).issubset(s):
            numbers[9] = s
        elif len(set(numbers[1]).difference(s)) == 1:
            numbers[6] = s
        else:
            numbers[0] = s

    for s in five_len:
        if set(numbers[1]).issubset(s):
            numbers[3] = s
        elif len(set(numbers[4]).difference(s)) == 2:
            numbers[2] = s
        else:
            numbers[5] = s

    return numbers


def part_two():
    output_value = 0
    for unique_signals, output_signals in read_input():
        numbers = get_numbers_map(unique_signals)
        decoded = ""
        for output_signal in output_signals:
            for number, signal in numbers.items():
                if set(signal) == set(output_signal):
                    decoded += str(number)

        output_value += int(decoded)

    return output_value


assert part_one() == 512
assert part_two() == 1091165
