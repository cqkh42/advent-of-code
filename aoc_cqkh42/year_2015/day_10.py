import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    number = None

    def part_a(self, iters=40):
        data = self.data
        for _ in range(iters):
            data = _look_and_see(data)
        self.number = data
        return len(data)

    def part_b(self, iters=10):
        data = self.number
        for _ in range(iters):
            data = _look_and_see(data)
        return len(data)


def _look_and_see(sequence):
    g = itertools.groupby(sequence)
    d = (f'{len(list(b))}{a}' for a, b in g)
    return ''.join(d)
