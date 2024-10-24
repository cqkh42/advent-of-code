import dataclasses
import itertools
import math
import re
from functools import cached_property

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph import a_star


class Solution(BaseSolution):
    def _process_data(self):
        indices = re.findall(r' (\w+) generator', self.input_)

        generators = [0 for _ in range(len(indices))]
        chips = [0 for _ in range(len(indices))]

        for floor_num, info in enumerate(self.lines):
            for gen in re.findall(r' (\w+) generator', info):
                index = indices.index(gen)
                generators[index] = floor_num
            for chip in re.findall(r' (\w+)-compatible', info):
                index = indices.index(chip)
                chips[index] = floor_num
        generators = tuple(generators)
        chips = tuple(chips)
        pairs = tuple(sorted((g, c) for g, c in zip(generators, chips)))
        g = Node(pairs, 0, 0)
        return g

    def part_a(self):
        pairs = tuple((3, 3) for _ in range(5))
        target = Node(pairs, 3, 0)
        z = a_star.AStar(self.processed, target)
        return z.run()

    def part_b(self):
        pairs = tuple((3, 3) for _ in range(7))
        target = Node(pairs, 3, 0)

        start_pairs = [*self.processed.pairs, (0, 0), (0, 0)]
        start_pairs = tuple(sorted(start_pairs))
        start = Node(start_pairs, 0, 0)
        z = a_star.AStar(start, target)
        return z.run()

@dataclasses.dataclass(frozen=True)
class Node(a_star.AStarBaseNode):
    pairs: tuple[tuple[int, int]]
    lift: int
    distance: int = dataclasses.field(compare=False, hash=False)

    @cached_property
    def generators(self):
        return tuple(i[0] for i in self.pairs)

    @cached_property
    def chips(self):
        return tuple(i[1] for i in self.pairs)

    def is_valid(self):
        if not 0 <= self.lift <= 3:
            return False

        if max(*self.chips, *self.generators) > 3:
            return False
        if min(*self.chips, *self.generators) < 0:
            return False

        # any loose chips on the same floor as a generator are toast
        loose_chips = {
            chip for gen, chip in zip(self.generators, self.chips)
            if gen != chip
        }
        # are any loose chips on the same floor as generators
        bad_gen = loose_chips.intersection(self.generators)
        return not bad_gen  # if non-zero, return true

    def neighbours(self):
        a = {i for i in self._neighbours() if i.is_valid() and i != self}
        yield from a

    def move_generators(self, indices, delta):
        t = [[g, c] for g,c in self.pairs]
        if isinstance(indices, int):
            t[indices][0] += delta
        else:
            for index in indices:
                t[index][0] += delta
        t = tuple(sorted((g, c) for g, c in t))
        return Node(t, self.lift + delta, self.distance+1)

    def _neighbours(self):
        # we can go up or down
        # we can move 1 or 2

        available_gens = [index for index, (gen, chip) in enumerate(self.pairs) if gen == self.lift]
        available_chips = [index for index, (gen, chip) in enumerate(self.pairs) if chip == self.lift]

        if self.lift == 0:
            floors = [1]
        elif self.lift == 3:
            floors = [-1]
        else:
            floors = [-1, 1]

        double_gens = itertools.combinations(available_gens, 2)
        yield from (self.move_generators(index, change) for index, change in itertools.product(available_gens, floors))
        yield from (self.move_generators(index, change) for index, change in itertools.product(double_gens, floors))

        double_chips = itertools.product(available_chips, repeat=2)
        double_chips = (c for c in double_chips if c[0] != c[1])
        for index, change in itertools.product((*([i] for i in available_chips), *double_chips), floors):
            c = list(self.chips)
            for i in index:
                c[i] += change
            if max(c) <= 3:
                pairs = tuple(sorted((a, b) for a, b in zip(self.generators, c)))
                yield Node(pairs, self.lift + change, self.distance + 1)

        for gen_index, chip_index, change in itertools.product(available_gens, available_chips, floors):
            c = list(self.chips)
            g = list(self.generators)
            c[chip_index] += change
            g[gen_index] += change
            if max(*g, *c) <= 3:
                pairs = tuple(sorted((a, b) for a, b in zip(g, c)))
                yield Node(pairs, self.lift + change, self.distance + 1)

    @cached_property
    def h(self):
        # trying to beat 157723, 157127, 157827
        steps = 0
        lift = self.lift
        things_on_zero_floor = [*self.chips, *self.generators].count(0)
        things_on_one_floor = [*self.chips, *self.generators].count(1) + things_on_zero_floor
        things_on_two_floor = [*self.chips, *self.generators].count(2) + things_on_one_floor

        if things_on_zero_floor:
            # take the lift down
            steps += (lift)
            trips = math.ceil(things_on_zero_floor / 2)
            steps += (2*(trips-1)) + 1
            lift = 1

        if things_on_one_floor:
            steps += abs(lift-1)
            trips = math.ceil(things_on_one_floor / 2)
            steps += (2 * (trips - 1)) + 1
            lift = 2

        if things_on_two_floor:
            steps += abs(lift-2)
            trips = math.ceil(things_on_two_floor / 2)
            steps += (2 * (trips - 1)) + 1
            lift = 3

        return steps

        return 3 - self.lift


if __name__ == "__main__":
    submit_answers(Solution, 11, 2016)
