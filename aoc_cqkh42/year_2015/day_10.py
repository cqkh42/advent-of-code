import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        self.sequence(40)
        return len(self.data)

    def part_b(self):
        self.sequence(10)
        return len(self.data)

    def iteration(self):
        g = itertools.groupby(self.data)
        d = (f'{len(list(b))}{a}' for a, b in g)
        self.data = ''.join(d)

    def sequence(self, iters):
        for _ in range(iters):
            self.iteration()
