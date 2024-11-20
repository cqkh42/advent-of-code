import itertools
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> list[list[int]]:
        return [[int(num) for num in row.split("\t")] for row in self.lines]

    def part_a(self):
        return sum(_row_checksum(row) for row in self.parsed)

    def part_b(self):
        return sum(_row_even_checksum(row) for row in self.parsed)


def _row_checksum(row):
    return max(row) - min(row)


def _row_even_checksum(values):
    perms = itertools.permutations(values, 2)
    solutions = (int(high / low) for high, low in perms if not high % low)
    return next(solutions)


if __name__ == "__main__":
    submit_answers(Solution, 2, 2017)
