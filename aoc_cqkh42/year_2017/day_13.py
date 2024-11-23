import itertools
from typing import Self

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def is_caught(time, size):
    return not time % (2 * size - 2)


class Solution(BaseSolution):
    PARSER = parse.compile('{:d}: {:d}')
    def _parse_line(self, line: str):
        return self.PARSER.search(line)

    def part_a(self):
        return sum(l * r for l, r in self.parsed_lines if is_caught(l, r))

    def part_b(self):
        for delay in itertools.count():
            locations = ((l + delay, r) for l, r in self.parsed_lines)
            if any(is_caught(l, r) for l, r in locations):
                continue
            else:
                return delay
        return None


if __name__ == "__main__":
    submit_answers(Solution, 13, 2017)
