import re
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        row, col = re.findall(r"\d+", self.input_)
        row = int(row)
        col = int(col)

        triangle_number = col + row - 1
        that_number = triangle_number * (triangle_number + 1) // 2
        my_number = that_number - row
        return (pow(252533, my_number, 33554393) * 20151125) % 33554393

    def part_b(self: Self) -> int:
        return 0


if __name__ == "__main__":
    submit_answers(Solution, 25, 2015)
