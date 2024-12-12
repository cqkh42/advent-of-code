import itertools

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution


def is_valid(x, y, z):
    a = x + y > z
    b = x + z > y
    c = y + z > x
    return a and b and c


class Solution(BaseSolution):
    def part_a(self):
        return sum(is_valid(*line) for line in self.line_numbers)

    def part_b(self):
        vertically = itertools.chain.from_iterable(zip(*self.line_numbers))
        return sum(is_valid(*line) for line in more_itertools.chunked(vertically, 3))
