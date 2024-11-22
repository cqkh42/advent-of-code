import parse
import sympy

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    PARSER = parse.compile("{:n} positions; at time=0, it is at position {:n}.")
    def _parse(self):
        firsts, seconds = zip(*self.parsed_lines)
        seconds = [idx + i for idx, i in enumerate(seconds, start=1)]
        return list(firsts), list(seconds)

    def _parse_line(self, line: str):
        return self.PARSER.search(line)

    def part_a(self):
        p = sympy.ntheory.modular.crt(*self.parsed)
        return p[1] - p[0]

    def part_b(self):
        first, second = self.parsed
        first.append(11)
        second.append(len(second) + 1)
        p = sympy.ntheory.modular.crt(first, second)
        return p[1] - p[0]


if __name__ == "__main__":
    submit_answers(Solution, 15, 2016)
