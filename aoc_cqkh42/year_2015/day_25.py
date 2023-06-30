import re
from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        row, col = re.findall(r"\d+", self.data)
        row = int(row)
        col = int(col)

        triangle_number = col + row - 1
        that_number = triangle_number * (triangle_number + 1) // 2
        my_number = that_number - row
        return (pow(252533, my_number, 33554393) * 20151125) % 33554393

    def part_b(self: Self) -> None:
        ...

    def _parse_data(self: Self) -> str:
        return self.data
