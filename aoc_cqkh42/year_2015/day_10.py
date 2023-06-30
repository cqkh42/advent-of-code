import itertools
from functools import cache

from aoc_cqkh42.helpers.base_solution import BaseSolution


@cache
def _resolve(a, b):
    return f"{len(list(b))}{a}"


class Solution(BaseSolution):
    def _iteration(self):
        g = itertools.groupby(self.data)
        d = (f"{len(list(b))}{a}" for a, b in g)
        self.data = "".join(d)

    def _sequence(self, iters):
        for _ in range(iters):
            self._iteration()
        return len(self.data)

    def part_a(self, iters=40):
        return self._sequence(iters)

    def part_b(self):
        return self._sequence(10)
