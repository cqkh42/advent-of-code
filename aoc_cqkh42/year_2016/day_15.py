import parse
import sympy

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self):
        p = parse.findall(
            '{:n} positions; at time=0, it is at position {:n}.',
            self.input_
        )
        firsts, seconds = zip(*p)
        seconds = [idx + i for idx, i in enumerate(seconds, start=1)]
        return list(firsts), list(seconds)

    def part_a(self):
        p = sympy.ntheory.modular.crt(*self.processed)
        return p[1] - p[0]

    def part_b(self):
        first, second = self.processed
        first.append(11)
        second.append(len(second) + 1)
        p = sympy.ntheory.modular.crt(first, second)
        return p[1] - p[0]


if __name__ == "__main__":
    submit_answers(Solution, 15, 2016)