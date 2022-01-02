import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def _iteration(self):
        g = itertools.groupby(self.data)
        d = (f'{len(list(b))}{a}' for a, b in g)
        self.data = ''.join(d)

    def _sequence(self, iters):
        for _ in range(iters):
            self._iteration()

    def part_a(self, iters=40):
        self._sequence(iters)
        return len(self.data)

    def part_b(self):
        self._sequence(10)
        return len(self.data)


