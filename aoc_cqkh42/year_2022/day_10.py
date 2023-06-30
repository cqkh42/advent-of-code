import itertools

import more_itertools

from aoc_cqkh42.helpers import aocr
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        r = more_itertools.flatten(
            (0,) if row == 'noop' else (0, int(row.split()[1]))
            for row in self.lines
        )
        x = list(itertools.accumulate((1, *r)))
        return x

    def part_a(self):
        return sum(
            i * self.parsed_data[i - 1]
            for i in [20, 60, 100, 140, 180, 220]
        )

    def part_b(self):
        result = [
            sprite - 1 <= index % 40 <= sprite + 1
            for index, sprite in enumerate(self.parsed_data[:-1])
        ]
        return aocr.word(result, True)
