import itertools
import re
import queue

import numpy as np


class State:
    def __init__(self, generators, chips, lift, g):
        self.generators = generators
        self.chips = chips
        self.lift = lift
        self.g = g

    def h(self):
        total = 0
        on_first = (self.generators == 1).sum() + (self.chips == 1).sum()
        on_second = (self.generators == 2).sum() + (self.chips == 2).sum()
        on_third = (self.generators == 3).sum() + (self.chips == 3).sum()
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
        g = self.generators
        c = self.chips
        z = tuple(sorted((str(a) + str(b) for a, b in zip(g, c))))
        return hash((z, self.lift))

    def is_valid(self):
        a = self.generators != self.chips
        b = self.chips[a].astype(int)
        loose_chips = set(b)
        return (not loose_chips.intersection(
            self.generators)) and self.lift in range(1, 5) and self.generators.max() <= 4 and self.generators.min() >=1 and self.chips.max() <= 4 and self.chips.min() >= 1

    def __eq__(self, other):
        return hash(self) == hash(other)

    def complete(self):
        a = np.array_equal(self.generators, self.chips)
        b = (self.generators == 4).all()
        return a and b

    def move_generator(self, index, floor, add_move=False):
        generators = self.generators.copy()
        c = self.chips.copy()
        generators[index] = floor
        if add_move:
            moves = self.g + 1
        else:
            moves = self.g
        return State(generators, c, floor, moves)

    def move_chip(self, index, floor, add_move=False):
        chips = self.chips.copy()
        g = self.generators.copy()
        chips[index] = floor
        if add_move:
            moves = self.g + 1
        else:
            moves = self.g
        return State(g, chips, floor, moves)

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
            m = State(up, self.chips.copy(), floor, self.g + 1)
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

        floor_single_chip = itertools.product(elev_moves, chips_on_floor)
        single_chip = {self.move_chip(chip, floor, True) for floor, chip in
                       floor_single_chip}
        next_moves.update(single_chip)

        floor_single_gen = itertools.product(elev_moves, generators_on_floor)
        single_gen = {self.move_generator(gen, floor, True) for floor, gen in
                      floor_single_gen}
        next_moves.update(single_gen)

        next_moves = {state for state in next_moves if state.is_valid()}
        return next_moves

    def __gt__(self, other):
        return self.priority > other.priority


def a_star(state):
    visited = set()
    to_visit = queue.PriorityQueue()
    to_visit.put(state)

    for turn in itertools.count():
        state = to_visit.get()
        if state.complete():
            print(turn)
            return state.g
        if state in visited:
            continue
        visited.add(state)
        new_states = state.new_moves()
        for new_state in new_states:
            to_visit.put(new_state)


def make_state(data):
    floors = data.split('\n')
    generators = [re.findall(r' (\w+) generator', floor) for floor in floors]
    generators = [[(element, floor) for element in elements] for floor, elements in (enumerate(generators, start=1)) if elements]
    generators = [floor for (element, floor) in sorted(itertools.chain.from_iterable(generators))]
    generators = np.array(generators)

    chips = [set(re.findall(r' (\w+)-compatible', floor)) for floor in floors]
    chips = [[(element, floor) for element in elements] for floor, elements in (enumerate(chips, start=1)) if elements]
    chips = [floor for (element, floor) in sorted(itertools.chain.from_iterable(chips))]
    chips = np.array(chips)
    return State(generators, chips, 1, 0)


def part_a(data):
    state = make_state(data)
    return a_star(state)


def part_b(data, **_):
    state = make_state(data)
    state.generators = np.append(state.generators, [1, 1])
    state.chips = np.append(state.chips, [1, 1])

    return a_star(state)
