import itertools
from typing import Self, Any

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

TRAPS = {
    "^^.":'^',
    ".^^":'^',
    "^..":'^',
    "..^": '^'
}


def calc_row(row):
    t = ["."] + row + ["."]
    triples = itertools.zip_longest(t, t[1:], t[2:], fillvalue=".")
    # triples = more_itertools.triplewise(t)
    new = [TRAPS.get(''.join(a), '.') for a in triples]
    new = new[:-2]
    return new


class Solution(BaseSolution):
    total = 0
    def _parse(self: Self) -> Any:
        self.total += self.input_.count('.')
        return list(self.input_)

    def _run(self, iters):
        for step in range(iters):
            self.parsed = calc_row(self.parsed)
            self.total += self.parsed.count(".")

    def part_a(self):
        self._run(39)
        return self.total

    def part_b(self):
        self._run(399_999 - 39)
        return self.total


if __name__ == "__main__":
    submit_answers(Solution, 18, 2016)
