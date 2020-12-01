import itertools


def part_a(data):
    return data.count('(') - data.count(')')


def part_b(data, **_):
    instructions = (1 if item == '(' else -1 for item in data)
    return list(itertools.accumulate(instructions)).index(-1) + 1
