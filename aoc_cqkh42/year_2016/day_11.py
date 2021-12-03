# TODO this is a mess
# TODO 2016 got to here and is broken
import itertools
import re

import numpy as np

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers.graph.bfs import BFS, BFSBaseState


class Solution(BaseSolution):
    def parse_data(self):
        generators = {}
        chips = {}

        for floor_num, info in enumerate(self.lines):
            for gen in re.findall(r' (\w+) generator', info):
                generators[gen] = floor_num
            for chip in re.findall(r' (\w+)-compatible', info):
                chips[chip] = floor_num
        generator_array = np.zeros((4, len(generators)), dtype='int')
        chip_array = np.zeros((4, len(generators)), dtype='int')
        for index, (element, floor) in enumerate(sorted(generators.items())):
            generator_array[floor, index] = 1
        for index, (element, floor) in enumerate(sorted(chips.items())):
            chip_array[floor, index] = 1
        lift_array = np.array([[1], [0], [0], [0]])
        arr = np.dstack([generator_array, chip_array]).astype(int)
        return State(arr, lift_array, 0)

    def part_a(self):
        z = BFS(self.parsed_data)
        return z.run()

    # def part_b(self):
    #     new_pair = Pair(1,1)
    #     self.parsed_data.pairs.extend([new_pair, new_pair])
    #     self.parsed_data.generators = np.append(self.parsed_data.generators, [1, 1])
    #     self.parsed_data.chips = np.append(self.parsed_data.chips, [1, 1])
    #
    #     return a_star(self.parsed_data)


def roll_array(array, slicer, num):
    arr = array.copy()
    arr[slicer] = np.roll(arr[slicer], num, axis=0)
    return arr


class State(BFSBaseState):
    def __init__(self, arr, lift, distance):
        self.arr = arr
        self.lift = lift
        self.distance = distance

    def is_target(self):
        return (self.arr[-1] == 1).all()

    def __hash__(self):
        return hash((self.arr.tostring(), self.lift.tostring()))

    def __eq__(self, other):
        a = (self.arr == other.arr).all()
        l = (self.lift == other.lift).all()
        return a and l

    @property
    def _floor(self):
        return np.argmax(self.lift)

    def neighbours(self):
        nn = set()
        # we go up
        if self._floor != 3:
            nn.update(self._moves(1))
        if self._floor != 0:
            nn.update(self._moves(-1))
        return nn

    def _moves(self, direction):
        nn = []
        new_lift = np.roll(self.lift, direction)

        moveable_gens = np.nonzero(self.arr[self._floor, :, 0])[0]
        moveable_chips = np.nonzero(self.arr[self._floor, :, 1])[0]
        all_combs = [
            (0, moveable_gens),
            (1, moveable_chips),
            (0, itertools.combinations(moveable_gens, 2)),
            (1, itertools.combinations(moveable_chips, 2)),
            ([0, 1], itertools.product(moveable_gens, moveable_chips))
        ]
        for gen_or_chip, options in all_combs:
            for option in options:
                s = (slice(None), option, gen_or_chip)
                new_arr = roll_array(self.arr, s, direction)
                new_neighbour = State(new_arr, new_lift,
                                      self.distance + 1)
                nn.append(new_neighbour)
        return {i for i in nn if i.is_valid()}

    def is_valid(self):
        chip = self.arr[:, :, 1]
        generator = self.arr[:, :, 0]
        loose_chip = chip & (generator != 1)
        loose_chip_floors = loose_chip.any(axis=1)
        generator_floors = generator.any(axis=1)
        return not (loose_chip_floors & generator_floors).any()

    # def h(self):
    #     total = 0
    #     on_first = sum(p.on(1) for p in self.pairs)
    #     on_second = sum(p.on(2) for p in self.pairs)
    #     on_third = sum(p.on(3) for p in self.pairs)
    #     if on_first:
    #         total += ((on_first-1) * 6) +3
    #     if on_second:
    #         total += ((on_second-1) * 4) +2
    #     if on_third:
    #         total += ((on_third-1) * 2) + 1
    #     return total

    # @property
    # def priority(self):
    #     return self.g + self.h()
