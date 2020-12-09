from aoc_cqkh42.year_2019.computer import Computer


def part_a(data):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]

    computer = Computer(inputs, [1])
    computer.run()
    return computer.output


def part_b(data, **_):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]

    computer = Computer(inputs, [2])
    computer.run()
    return computer.output
