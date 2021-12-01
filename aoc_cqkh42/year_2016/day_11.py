# TODO this is a mess
from dataclasses import dataclass, replace
import itertools
import re

import numpy as np

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers.dijkstra import a_star

def a(lines):
    generators = {}
    chips = {}
    for floor_num, info in enumerate(lines, start=1):
        gens = re.findall(r' (\w+) generator', info)
        for gen in gens:
            generators[gen] = floor_num
        chps = re.findall(r' (\w+)-compatible', info)
        for chip in chps:
            chips[chip] = floor_num
class Solution(BaseSolution):
    def parse_data(self):
        generators = {}
        chips = {}
        for floor_num, info in enumerate(self.lines, start=1):
            gens = re.findall(r' (\w+) generator', info)
            for gen in gens:
                generators[gen] = floor_num
            chps = re.findall(r' (\w+)-compatible', info)
            for chip in chps:
                chips[chip] = floor_num
        print(generators)

        floors = self.lines
        generators = [re.findall(r' (\w+) generator', floor) for floor in floors]
        print(dict(enumerate(generators, start=1)))
        generators = [[(element, floor) for element in elements] for floor, elements in (enumerate(generators, start=1))
                      if elements]
        generators = [floor for (element, floor) in sorted(itertools.chain.from_iterable(generators))]
        generators = np.array(generators)
        print(generators)

        chips = [set(re.findall(r' (\w+)-compatible', floor)) for floor in floors]
        chips = [[(element, floor) for element in elements] for floor, elements in (enumerate(chips, start=1)) if
                 elements]
        chips = [floor for (element, floor) in sorted(itertools.chain.from_iterable(chips))]
        chips = np.array(chips)

        pairs = [Pair(g, c) for g, c in zip(generators, chips)]
        # print(pairs)
        return State(pairs, 1, 0)

    def part_a(self):
        return a_star(self.parsed_data)

    def part_b(self):
        new_pair = Pair(1,1)
        self.parsed_data.pairs.extend([new_pair, new_pair])
        self.parsed_data.generators = np.append(self.parsed_data.generators, [1, 1])
        self.parsed_data.chips = np.append(self.parsed_data.chips, [1, 1])

        return a_star(self.parsed_data)


@dataclass(frozen=True, eq=True)
class Pair:
    generator: int
    chip: int

    def on(self, floor):
        return int(self.generator == floor) + int(self.chip == floor)

    def valid(self):
        gen = 1 <= self.generator <= 4
        chip = 1 <= self.chip <= 4
        return gen and chip

    def same(self):
        return self.generator == self.chip


class State:
    def __init__(self, pairs, lift, g):
        self.generators = np.array([pair.generator for pair in pairs])
        self.chips = np.array([pair.chip for pair in pairs])
        self.lift = lift
        self.g = g
        self.pairs = pairs

    def h(self):
        total = 0
        on_first = sum(p.on(1) for p in self.pairs)
        on_second = sum(p.on(2) for p in self.pairs)
        on_third = sum(p.on(3) for p in self.pairs)
        if on_first:
            total += ((on_first-1) * 6) +3
        if on_second:
            total += ((on_second-1) * 4) +2
        if on_third:
            total += ((on_third-1) * 2) + 1
        return total

    @property
    def priority(self):
        return self.g + self.h()

    def __hash__(self):
        # TODO there must be a better way
        z = sorted(self.pairs, key=lambda pair: (pair.generator, pair.chip))
        z = tuple(z)
        return hash((z, self.lift))

    def is_valid(self):
        # what floors are the loose chips on
        # are there generators on there
        loose_chips = {pair.chip for pair in self.pairs if not pair.same()}
        gens = {pair.generator for pair in self.pairs}
        pieces = all(pair.valid() for pair in self.pairs)

        return (not loose_chips.intersection(gens)) and 1 <= self.lift <= 4 and pieces

    def __eq__(self, other):
        return hash(self) == hash(other)

    def complete(self):
        return all(pair.on(4) == 2 for pair in self.pairs)

    def move_generator(self, index, floor, add_move=False):
        local_pairs = [p for p in self.pairs]
        new = replace(local_pairs[index], generator=floor)
        local_pairs[index] = new
        return State(local_pairs, floor, self.g+add_move)

    def move_chip(self, index, floor, add_move=False):
        local_pairs = [p for p in self.pairs]
        new = replace(local_pairs[index], chip=floor)
        local_pairs[index] = new
        return State(local_pairs, floor, self.g+add_move)

    def new_moves(self):
        lowest = min(*[int(gen) for gen in self.generators], *[int(chip) for chip in self.chips])
        elev_moves = [
            floor for floor in [self.lift-1,self.lift+1]
            if floor >= lowest and floor in range(1, 5)
        ]
        next_moves = set()

        generators_on_floor = np.where(self.generators == self.lift)[0]
        chips_on_floor = np.where(self.chips == self.lift)[0]

        two_generator_combinations = itertools.combinations(
            generators_on_floor, 2)

        floor_gen_product = itertools.product(elev_moves,
                                              two_generator_combinations)
        for floor, (g_1, g_2) in floor_gen_product:
            up = self.generators.copy()
            up[[g_1, g_2]] = floor
            pairs = [Pair(g_, c_) for g_, c_ in zip(up, self.chips.copy())]

            m = State(pairs, floor, self.g + 1)
            next_moves.add(m)

        two_chip_combinations = itertools.combinations(chips_on_floor, 2)
        floor_chip_product = itertools.product(elev_moves,
                                               two_chip_combinations)
        two_chips = {
            self.move_chip(chip_1, floor, False).move_chip(chip_2, floor, True)
            for floor, (chip_1, chip_2) in floor_chip_product
        }
        next_moves.update(two_chips)

        chip_and_gen_combinations = itertools.product(chips_on_floor,
                                                      generators_on_floor)
        floor_chip_gen = itertools.product(elev_moves,
                                           chip_and_gen_combinations)
        chip_and_gen = {
            self.move_chip(chip, floor, False).move_generator(gen, floor, True)
            for floor, (chip, gen) in floor_chip_gen
        }
        next_moves.update(chip_and_gen)

        # for each pair
        gens_to_move = [index for index, pair in enumerate(self.pairs) if pair.generator == self.lift]
        for index in gens_to_move:
            for direction in [-1, 1]:
                local_pair = [pair for pair in self.pairs]
                new_pair = replace(self.pairs[index], generator=self.lift + direction)
                local_pair[index] = new_pair
                state = State(local_pair, self.lift + direction, self.g + 1)
                next_moves.add(state)


        for index, pair in enumerate(self.pairs):
            local_pair = [pair for pair in self.pairs]
            if pair.chip == self.lift:
                for direction in [1, -1]:
                    new_pair = replace(pair, chip=self.lift+direction)
                    local_pair[index] = new_pair
                    state = State(local_pair, self.lift+direction, self.g + 1)
                    next_moves.add(state)
        # I move both things
            local_pair = [pair for pair in self.pairs]
            if pair.on(self.lift) == 2:
                for direction in [1, -1]:
                    new_pair = replace(pair, chip=self.lift+direction, generator=self.lift+direction)
                    local_pair[index] = new_pair
                    state = State(local_pair, self.lift+direction, self.g + 1)
                    next_moves.add(state)


        next_moves = {state for state in next_moves if state.is_valid()}
        return next_moves

    def __gt__(self, other):
        return self.priority > other.priority


