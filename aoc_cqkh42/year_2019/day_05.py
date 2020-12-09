from aoc_cqkh42.year_2019.computer import Computer


def part_a(data):
    intcode = [int(num) for num in data.split(',')]
    computer = Computer(intcode, [1])
    computer.run()
    return computer.outputs.pop()


def part_b(data, **_):
    intcode = [int(num) for num in data.split(',')]
    c = Computer(intcode, [5])
    c.run()
    return c.outputs.pop()
