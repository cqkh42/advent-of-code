import itertools


def part_a(data):
    jumps = [int(num) for num in data.split('\n')]
    index = 0
    for step in itertools.count(0):
        try:
            new_index = index + jumps[index]
        except IndexError:
            return step
        else:
            jumps[index] += 1
            index = new_index


def part_b(data, **_):
    jumps = [int(num) for num in data.split('\n')]
    index = 0
    for step in itertools.count(0):
        try:
            new_index = index + jumps[index]
        except IndexError:
            return step
        else:
            jumps[index] += (-1) ** (jumps[index] >= 3)
            index = new_index
