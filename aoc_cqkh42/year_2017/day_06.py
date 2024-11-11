import functools
import itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def _distribute(banks):
    banks = list(banks)
    being_distributed = banks.index(max(banks))
    to_distribute = banks[being_distributed]
    banks[being_distributed] = 0
    for block in range(to_distribute):
        index = (block + being_distributed + 1) % len(banks)
        banks[index] += 1
    return tuple(banks)


class Solution(BaseSolution):
    def part_a(self):
        return do(self.numbers)[0]

    def part_b(self):
        a = do(self.numbers)
        return a[0] - a[1]


@functools.cache
def do(banks):
    seen = {banks: 1}
    for dist in itertools.count(1):
        banks = _distribute(banks)
        if banks in seen:
            return dist, seen[banks]
        seen[banks] = dist


if __name__ == "__main__":
    submit_answers(Solution, 6, 2017)
