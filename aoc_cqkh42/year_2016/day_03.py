import itertools

import more_itertools
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


def is_valid(x, y, z):
    a = x + y > z
    b = x + z > y
    c = y + z > x
    return a and b and c


class Solution(BaseSolution):
    PARSER = parse.compile("{:>d} {:>d} {:>d}")
    def _parse_line(self, line: str):
        return self.PARSER.search(line)

    def part_a(self):
        return sum(is_valid(*line) for line in self.parsed_lines)

    def part_b(self):
        vertically = itertools.chain.from_iterable(zip(*self.parsed_lines))
        return sum(is_valid(*line) for line in more_itertools.chunked(vertically, 3))
