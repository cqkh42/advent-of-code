import itertools

from aoc_cqkh42.year_2019 import computer


def part_a(data):
    intcode = computer.parse_string(data)
    intcode[1] = 12
    intcode[2] = 2
    return computer.get_output(intcode)


def part_b(data, **_):
    for noun, verb in itertools.product(range(100), range(100)):
        intcode = computer.parse_string(data)
        intcode[1] = noun
        intcode[2] = verb
        if computer.get_output(intcode) == 19690720:
            return 100 * noun + verb
