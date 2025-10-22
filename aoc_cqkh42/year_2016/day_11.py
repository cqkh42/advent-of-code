import dataclasses
import itertools
import re
from dataclasses import dataclass

from typing import Iterable, Self
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph import a_star

@dataclass
class ChipPair:
    microchip: int
    generator: int

    def __hash__(self):
        return hash((self.microchip, self.generator))

    def is_valid(self):
        return (0 <= self.microchip <= 3) and (0 <= self.generator <= 3)

    def distance(self):
        return max((3-self.microchip, 3-self.generator))

@dataclass(eq=True, frozen=True)
class ChipSet:
    pairs: Iterable[ChipPair]
    lift: int = 0

    def __hash__(self):
        pairs = sorted((pair.microchip, pair.generator) for pair in self.pairs)
        all_ = tuple((*pairs, self.lift))

        return hash(all_)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, item):
        return self.pairs[item]

    def is_valid(self):
        if not 0 <= self.lift <= 3:
            return False

        if not all(pair.is_valid() for pair in self.pairs):
            return False

        # any loose chips on the same floor as a generator are toast
        loose_chips = {
            pair.microchip for pair in self.pairs if pair.generator != pair.microchip
        }
        generators = {pair.generator for pair in self.pairs}
        # are any loose chips on the same floor as generators
        bad_gen = loose_chips.intersection(generators)
        return not bad_gen  # if non-zero, return true

class Solution(BaseSolution):
    def _parse(self):
        generator_dict = {}
        chip_dict = {}
        for index, line in enumerate(self.lines):
            for generator in re.findall(r" (\w+) generator", line):
                generator_dict[generator] = index
            for chip in re.findall(r" (\w+)-compatible", line):
                chip_dict[chip] = index
        pairs = []
        for key in generator_dict:
            pairs.append(ChipPair(chip_dict[key], generator_dict[key]))
        chipset = ChipSet(pairs)
        return Node(chipset, 0)

    def part_a(self):
        z = a_star.AStar(self.parsed)
        return z.run()

    def part_b(self):
        new_chipset = self.parsed.chip_set.pairs + [ChipPair(0,0), ChipPair(0,0)]
        new_node = Node(ChipSet(new_chipset), 0)
        z = a_star.AStar(new_node)
        return z.run()


@dataclasses.dataclass
class Node(a_star.BaseNode):
    chip_set: ChipSet
    distance: int

    def h(self):
        return max(pair.distance() for pair in self.chip_set.pairs)

    def __eq__(self, other: Self):
        return self.chip_set == other.chip_set

    def __hash__(self):
        return hash(self.chip_set)

    def pairs(self):
        return self.chip_set.pairs

    def is_target(self):
        return set(self.pairs()) == {ChipPair(3,3)}

    def neighbours(self):
        a = {i for i in self._neighbours() if i.chip_set.is_valid()}
        yield from a

    def _move_chip(self, index, floor, increase_distance=True):
        existing_pair = self.chip_set.pairs[index]
        new_pair = ChipPair(microchip=floor, generator = existing_pair.generator)
        new_chipset = self.chip_set.pairs.copy()
        new_chipset[index] = new_pair
        return Node(ChipSet(new_chipset, floor), self.distance+increase_distance)

    def _move_generator(self, index, floor, increase_distance=True):
        existing_pair = self.chip_set.pairs[index]
        new_pair = ChipPair(generator=floor, microchip = existing_pair.microchip)
        new_chipset = self.chip_set.pairs.copy()
        new_chipset[index] = new_pair
        return Node(ChipSet(new_chipset, floor), self.distance+increase_distance)

    def _neighbours(self):
        # we can go up or down
        # we can move 1 or 2

        if self.chip_set.lift == 0:
            floors = [1]
        elif self.chip_set.lift == 3:
            floors = [2]
        else:
            floors = [self.chip_set.lift +1, self.chip_set.lift-1]

        for a_index, b_index in itertools.permutations(range(len(self.chip_set)), 2):
            for floor in floors:
                a = self.chip_set[a_index]
                b = self.chip_set[b_index]

                if a.microchip == self.chip_set.lift:
                    moved = self._move_chip(a_index, floor, True)
                    if b.microchip == self.chip_set.lift:
                        yield moved._move_chip(b_index, floor, False)
                    if b.generator == self.chip_set.lift:
                        yield moved._move_generator(b_index, floor, False)
                    if a.generator == self.chip_set.lift:
                        yield moved._move_generator(a_index, floor, False)
                    yield moved
                if a.generator == self.chip_set.lift:
                    moved = self._move_generator(a_index, floor, True)
                    if b.generator == self.chip_set.lift:
                        yield moved._move_generator(b_index, floor, False)
                    if b.microchip == self.chip_set.lift:
                        yield moved._move_chip(b_index, floor, False)
                    yield moved


if __name__ == "__main__":
    submit_answers(Solution, 11, 2016)
