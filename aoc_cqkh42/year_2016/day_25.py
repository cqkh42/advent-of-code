from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2016.day_12 import Computer


class Solution(BaseSolution):
    def part_a(self: Self) -> str | int:
        for i in range(190):
            c = Computer(self.input_)
            c['a'] = i
            c.run()
            if sum(c.outputs) == (len(c.outputs) / 2):
                return i

    def part_b(self: Self) -> str | int:
        return
