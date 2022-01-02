# TODO this is a mess
# TODO 2016 got to here and is broken

# TODO this runs but takes forever
import dataclasses
import itertools
import re

import numpy as np

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers.graph.bfs import BFS, BFSBaseState
from aoc_cqkh42.helpers.graph import a_star


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
class State(a_star.AStarBaseState):
    arr: np.array
    lift: np.array
    distance: int = dataclasses.field(compare=False, hash=False)

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

    def h(self):
        return 0
        # a = self.arr[0,:,:].sum()
        # b = self.arr[1, :, :].sum()
        # c = self.arr[2, :, :].sum()
        #
        # return (a * 3) + (b*2) + c
        # return 3 - self._floor
        # return 0
        # stuff_on_floor = self.arr.sum(axis=1)
        # trips = stuff_on_floor // 2

        # go down to lowest floor
        # have to bring something down there
        # bring stuff up one at a time (you have to go back down for it)

        total = 0
        on_first = self.arr[0,:,:].sum()
        on_second = self.arr[1,:,:].sum()
        on_third = self.arr[2,:,:].sum()

        if on_first:
            total += ((on_first-1) * 6) +3
        if on_second:
            total += ((on_second-1) * 4) +2
        if on_third:
            total += ((on_third-1) * 2) + 1
        return total

    # @property
    # def priority(self):
    #     return self.g + self.h()
