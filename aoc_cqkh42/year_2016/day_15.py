import parse
from sympy.ntheory.modular import crt

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse_data(self):
        p = parse.findall(
            '{:n} positions; at time=0, it is at position {:n}.',
            self.data
        )
        firsts, seconds = zip(*p)
        seconds = [idx + i for idx, i in enumerate(seconds, start=1)]
        return list(firsts), list(seconds)

    def part_a(self):
        p = crt(*self.parsed_data)
        return p[1] - p[0]

    def part_b(self):
        first, second = self.parsed_data
        first.append(11)
        second.append(len(second) + 1)
        p = crt(first, second)
        return p[1] - p[0]
