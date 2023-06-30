from typing import Self

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def solve(self, size):
        is_unique = more_itertools.first_true(
            enumerate(more_itertools.windowed(self.input_, size), start=size),
            pred=lambda x: more_itertools.all_unique(x[1])
        )
        return is_unique[0]

    def part_a(self):
        return self.solve(4)

    def part_b(self):
        return self.solve(14)

    def _process_data(self: Self) -> str:
        return self.input_
