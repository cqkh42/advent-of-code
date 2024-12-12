import itertools
import operator

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        return sum(_row_checksum(row) for row in self.line_numbers)

    def part_b(self):
        return sum(_row_even_checksum(row) for row in self.line_numbers)


def _row_checksum(row):
    return -operator.sub(*more_itertools.minmax(row))


def _row_even_checksum(values):
    perms = itertools.permutations(values, 2)
    solutions = (int(high / low) for high, low in perms if not high % low)
    return more_itertools.first(solutions)


if __name__ == "__main__":
    submit_answers(Solution, 2, 2017)
