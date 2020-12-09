import itertools

from aoc_cqkh42.year_2019.computer import Computer


def part_a(data):
    intcode = [int(num) for num in data.split(',')]
    intcode[1] = 12
    intcode[2] = 2
    computer = Computer(intcode, [])
    computer.run()
    return computer.intcode[0]


def part_b(data, **_):
    for noun, verb in itertools.product(range(100), range(100)):
        intcode = [int(num) for num in data.split(',')]
        intcode[1] = noun
        intcode[2] = verb
        computer = Computer(intcode, [])
        computer.run()
        if computer.intcode[0] == 19690720:
            return 100 * noun + verb
