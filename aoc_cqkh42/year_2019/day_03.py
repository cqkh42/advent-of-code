from functools import cached_property

import numpy as np
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile("{:l}{:d}")
    wire_1 = None
    wire_2 = None

    def _parse_data(self):
        self.wire_1 = self._build_route(self.lines[0])
        self.wire_2 = self._build_route(self.lines[1])

    def _build_route(self, route):
        mapping = {
            'R': np.array([[1, 0]]),
            'L': np.array([[-1, 0]]),
            'U': np.array([[0, 1]]),
            'D': np.array([[0, -1]])
        }
        steps = np.concatenate([
            mapping[direction].repeat(steps, axis=0)
            for direction, steps in self.parser.findall(route)
        ])
        steps = np.add.accumulate(steps)
        return steps

    @cached_property
    def intersections(self):
        w_1 = {tuple(i) for i in self.wire_1.tolist()}
        w_2 = {tuple(i) for i in self.wire_2.tolist()}
        return w_1.intersection(w_2)

    def part_a(self):
        return min(abs(x) + abs(y) for x, y in self.intersections)

    def part_b(self):
        return min(
            np.argmax((self.wire_1 == i).all(axis=1)) +
            np.argmax((self.wire_2 == i).all(axis=1)) + 2
            for i in self.intersections
        )
