# TODO this is a mess
# TODO 2016 got to here and is broken

# TODO this runs but takes forever
import dataclasses
import itertools
import re

import numpy as np

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph import a_star


class Solution(BaseSolution):
    def parse_data(self):
        indices = re.findall(r' (\w+) generator', self.data)

        generators = np.zeros(len(indices), dtype=int)
        chips = np.zeros(len(indices), dtype=int)

        for floor_num, info in enumerate(self.lines):
            for gen in re.findall(r' (\w+) generator', info):
                index = indices.index(gen)
                generators[index] = floor_num
            for chip in re.findall(r' (\w+)-compatible', info):
                index = indices.index(chip)
                chips[index] = floor_num
        return Node(generators, chips, 0, 0)

    def part_a(self):
        # return None
        z = a_star.AStar(self.parsed_data)
        return z.run()

    def part_b(self):
        return None
        # new = np.zeros((4, 2, 2), dtype=int)
        # new[0] = 1
        # arr = np.concatenate([self.parsed_data.arr, new], axis=1)
        # state = State(arr, np.array([1, 0, 0, 0]), 0)
        # print(arr[:,:,0])
        # print(arr[:,:,1])
        # z = a_star.AStar(state)
        # return z.run()


def roll_array(array, slicer, num):
    arr = array.copy()
    arr[slicer] = np.roll(arr[slicer], num, axis=0)
    return arr


@dataclasses.dataclass
class Node(a_star.AStarBaseNode):
    generators: np.array
    chips: np.array
    lift: int
    distance: int = dataclasses.field(compare=False, hash=False)

    def __hash__(self):
        return hash((self.generators.tostring(), self.chips.tostring(), self.lift))

    def is_target(self):
        return (self.generators == 3).all() and (self.chips == 3).all()

    def __eq__(self, other):
        return (
            (self.generators == other.generators).all() and
            (self.chips == other.chips).all() and
            self.lift == other.lift
        )

    def is_valid(self):
        if not 0 <= self.lift <= 3:
            return False
        loose_chips = {chip for gen, chip in zip(self.generators, self.chips) if gen != chip}
        bad_gen = loose_chips.intersection(self.generators)
        return not bad_gen

        print(loose_chips, self.generators, bad_gen)
        # prin
        # print(self.chips, self.generators)
        # return True
        # if a chip is with another RTG and not its own, it will be fried
        # return any(chip in self.generators for chip in loose_chips)

        for gen, chip in zip(self.generators, self.chips):
            if gen != chip and chip in self.generators:
                return False
        return True

    def neighbours(self):
        a = {i for i in self._neighbours() if i.is_valid()}
        yield from a

    def _neighbours(self):
        # we can go up or down
        # we can move 1 or 2

        available_gens = np.flatnonzero(self.generators == self.lift)
        available_chips = np.flatnonzero(self.chips == self.lift)

        double_gens = (list(indices) for indices in itertools.combinations(available_gens, 2))
        for index, change in itertools.product((*available_gens, *double_gens), (-1, 1)):
            g = self.generators.copy()
            g[index] += change
            yield Node(g, self.chips, self.lift + change, self.distance + 1)

        double_chips = (list(indices) for indices in itertools.combinations(available_chips, 2))
        for index, change in itertools.product((*available_chips, *double_chips), (-1, 1)):
            c = self.chips.copy()
            c[index] += change
            yield Node(self.generators, c, self.lift + change, self.distance + 1)

        for gen_index, chip_index, change in itertools.product(available_gens, available_chips, (-1, 1)):
            c = self.chips.copy()
            g = self.generators.copy()
            c[chip_index] += change
            g[gen_index] += change
            yield Node(g, c, self.lift + change, self.distance + 1)

    def h(self):
        return 0
