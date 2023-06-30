import itertools
import math

import more_itertools

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
    def _parse_data(self):
        return frozenset(self.numbers)

    def solve(self, num_groups):
        groups = sets_sum_to(
            self.parsed_data, sum(self.parsed_data) / num_groups, num_groups
        )
        return min(math.prod(i) for i in groups if len(i) == len(min(groups, key=len)))

    def part_a(self):
        return self.solve(3)

    def part_b(self):
        return self.solve(4)
