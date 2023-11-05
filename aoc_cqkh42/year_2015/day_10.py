import itertools
from functools import cache

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@cache
def _resolve(a, b):
    return f"{len(list(b))}{a}"


class Solution(BaseSolution):
    def _iteration(self):
        g = itertools.groupby(self.input_)
        d = (f"{len(list(b))}{a}" for a, b in g)
        self.input_ = "".join(d)

    def _sequence(self, iters):
        for _ in range(iters):
            self._iteration()
        return len(self.input_)

    def part_a(self, iters=40):
        return self._sequence(iters)

    def part_b(self):
        return self._sequence(10)


if __name__ == "__main__":
    submit_answers(Solution, 10, 2015)
