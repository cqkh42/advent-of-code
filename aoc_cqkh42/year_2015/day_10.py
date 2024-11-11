import itertools
from functools import cache

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@cache
def _resolve(a, b):
    return f"{len(list(b))}{a}"


def iterate(string):
    g = itertools.groupby(string)
    d = (f"{len(list(b))}{a}" for a, b in g)
    return "".join(d)


class Solution(BaseSolution):
    def _sequence(self, iters):
        string = self.input_
        for _ in range(iters):
            string = iterate(string)
        return string

    def part_a(self, iters=40):
        self.input_ = self._sequence(iters)
        return len(self.input_)

    def part_b(self):
        return len(self._sequence(10))


if __name__ == "__main__":
    submit_answers(Solution, 10, 2015)
