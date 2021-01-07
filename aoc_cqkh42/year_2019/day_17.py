import itertools

import numpy as np

from aoc_cqkh42.year_2019.computer import Computer


def horizontal_intersections(scaffolding):
    left = np.pad(scaffolding,((0,0),(1,0)), mode='constant', constant_values='.')[:, :-1]
    right = np.pad(scaffolding,((0,0),(0,1)), mode='constant', constant_values='.')[:, 1:]
    return (left == right) & (left == scaffolding) & (scaffolding == '#')


def vertical_intersections(scaffolding):
    above = np.pad(scaffolding,((1,0),(0,0)), mode='constant', constant_values='.')[:-1]
    below = np.pad(scaffolding, ((0, 1), (0, 0)), mode='constant')[1:]
    return (above == below) & (above == scaffolding) & (scaffolding == '#')


def build_scaffolding(intcode):
    computer = Computer(intcode, [])
    computer.run()
    scaffolding = computer.outputs
    scaffolding = "".join([chr(i) for i in scaffolding])
    scaffolding = scaffolding.split("\n")[:-2]
    sc = [list(i) for i in scaffolding]

    return np.array(sc)


def part_a(data):
    inputs = data.split(",")
    intcode = [int(input_) for input_ in inputs]
    scaffolding = build_scaffolding(intcode)

    hors = horizontal_intersections(scaffolding)
    vert = np.array(vertical_intersections(scaffolding))
    common = np.argwhere((hors == vert) & hors)
    prods = common.prod(axis=1)
    return prods.sum()


def current_location(sc):
    for a, row in enumerate(sc):
        for c, item in enumerate(row):
            if item in ["^", ">", "v", "<"]:
                return a, c


def part_b(data, **_):
    return False
    intcode = [int(input_) for input_ in data.split(',')]
    scaffolding = build_scaffolding(intcode)

    # print('\n')
    # for row in scaffolding:
    #     print(''.join(row))

    # start_location = np.

