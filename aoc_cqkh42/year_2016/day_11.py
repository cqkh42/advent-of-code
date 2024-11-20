import dataclasses
import itertools
import re

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph import a_star


class Solution(BaseSolution):
    def _parse(self):
        indices = re.findall(r" (\w+) generator", self.input_)

        generators = [0 for _ in range(len(indices))]
        chips = [0 for _ in range(len(indices))]

        for floor_num, info in enumerate(self.lines):
            for gen in re.findall(r" (\w+) generator", info):
                index = indices.index(gen)
                generators[index] = floor_num
            for chip in re.findall(r" (\w+)-compatible", info):
                index = indices.index(chip)
                chips[index] = floor_num
        generators = list(generators)
        chips = list(chips)
        g = Node(generators, chips,  0, 0)
        return g

    def part_a(self):
        z = a_star.AStar(self.parsed)
        return z.run()

    def part_b(self):
        gen = [*self.parsed.generators, 0, 0]
        chips = [*self.parsed.chips, 0, 0]
        start = Node(gen, chips, 0, 0)
        z = a_star.AStar(start)
        return z.run()


@dataclasses.dataclass
class Node(a_star.BaseNode):
    generators: list[int, ...]
    chips: list[int, ...]
    lift: int
    distance: int

    def __eq__(self, other):
        p = sorted((g, c) for g, c in self.pairs())
        other_p = sorted((g, c) for g, c in other.pairs())
        return p == other_p and self.lift == other.lift

    def __hash__(self):
        p = sorted((g, c) for g, c in self.pairs())
        return hash(tuple(p))

    def pairs(self):
        return tuple(zip(self.generators, self.chips))

    def is_target(self):
        return set(self.pairs()) == {(3,3)} and self.lift == 3

    def is_valid(self):
        if not 0 <= self.lift <= 3:
            return False

        if max(*self.chips, *self.generators) > 3:
            return False
        if min(*self.chips, *self.generators) < 0:
            return False

        # any loose chips on the same floor as a generator are toast
        loose_chips = {
            chip for gen, chip in self.pairs() if gen != chip
        }
        # are any loose chips on the same floor as generators
        bad_gen = loose_chips.intersection(self.generators)
        return not bad_gen  # if non-zero, return true

    def neighbours(self):
        a = {i for i in self._neighbours() if i.is_valid()}
        yield from a

    def move(self, indices, delta, arr, field):
        for index in more_itertools.always_iterable(indices):
            arr[index] += delta
        return dataclasses.replace(
            self,
            lift=self.lift+delta,
            distance=self.distance+1,
            **{field:arr}
        )

    def _neighbours(self):
        # we can go up or down
        # we can move 1 or 2

        available_gens = [
            index for index, gen in enumerate(self.generators) if gen == self.lift
        ]
        available_chips = [
            index for index, chip in enumerate(self.chips) if chip == self.lift
        ]

        if self.lift == 0:
            floors = [1]
        elif self.lift == 3:
            floors = [-1]
        else:
            floors = [-1, 1]

        double_gens = list(itertools.combinations(available_gens, 2))
        double_chips = list(itertools.combinations(available_chips, 2))
        yield from (
            self.move(index, change, list(self.generators), 'generators')
            for index, change in itertools.product(available_gens + double_gens, floors)
        )


        yield from (
            self.move(index, change, list(self.chips), 'chips')
            for index, change in
        itertools.product(available_chips + double_chips, floors)
        )

        for gen_index, chip_index, change in itertools.product(
            available_gens, available_chips, floors
        ):
            a = self.move(gen_index, change, list(self.generators), 'generators')
            yield a.move(chip_index, change,list(self.chips), 'chips')


if __name__ == "__main__":
    submit_answers(Solution, 11, 2016)
