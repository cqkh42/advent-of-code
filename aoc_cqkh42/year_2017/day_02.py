import itertools
import operator
from typing import Self

import more_itertools
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    PARSER = parse.compile('{:d}')
    def _parse_line(self, line: str):
        return [i[0] for i in self.PARSER.findall(line)]

    def part_a(self):
        return sum(_row_checksum(row) for row in self.parsed_lines)

    def part_b(self):
        return sum(_row_even_checksum(row) for row in self.parsed_lines)


def _row_checksum(row):
    return -operator.sub(*more_itertools.minmax(row))


def _row_even_checksum(values):
    perms = itertools.permutations(values, 2)
    solutions = (int(high / low) for high, low in perms if not high % low)
    return more_itertools.first(solutions)


if __name__ == "__main__":
    submit_answers(Solution, 2, 2017)
