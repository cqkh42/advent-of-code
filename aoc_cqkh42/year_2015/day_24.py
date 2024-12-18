import itertools
import math

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def subsets_equal_to(set_, target):
    for size in range(1, len(set_) + 1):
        combs = itertools.combinations(set_, size)
        for comb in combs:
            if sum(comb) == target:
                return comb


def sets_sum_to(set_, target, num):
    if num == 1:
        return [subsets_equal_to(set_, target)]
    else:
        a = sets_sum_to(set_, target, num - 1)
        next_ = subsets_equal_to(set_.difference(a), target)
        return *more_itertools.always_iterable(a), next_


class Solution(BaseSolution):
    def solve(self, num_groups):
        numbers = self.numbers_as(frozenset)
        groups = sets_sum_to(
            numbers, sum(numbers) / num_groups, num_groups
        )
        return min(math.prod(i) for i in groups if len(i) == len(min(groups, key=len)))

    def part_a(self):
        return self.solve(3)

    def part_b(self):
        return self.solve(4)


if __name__ == "__main__":
    submit_answers(Solution, 24, 2015)
