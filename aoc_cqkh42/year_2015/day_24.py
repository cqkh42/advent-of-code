# TODO really messy
import itertools
import math

import more_itertools

from aoc_cqkh42 import BaseSolution


def subsets_equal_to(set_, target):
    for size in range(1, len(set_)+1):
        combs = itertools.combinations(set_, size)
        yield from (comb for comb in combs if sum(comb) == target)

def two_sets_sum_to(set_, target):
    for first in subsets_equal_to(set_, target):
        second = subsets_equal_to(set_.difference(first), target)
        for s in second:
            yield first, s

def sets_sum_to(set_, target, num):
    if num == 1:
        yield from subsets_equal_to(set_, target)
    elif num == 2:
        for first in subsets_equal_to(set_, target):
            second = subsets_equal_to(set_.difference(first), target)
            for s in second:
                yield first, s
    else:
        for results in sets_sum_to(set_, target, num-1):
            next_ = subsets_equal_to(set_.difference(*results), target)
            for t in next_:
                yield *more_itertools.always_iterable(results), t

class Solution(BaseSolution):
    def parse_data(self):
        return frozenset(self.numbers)

    def solve(self, num_groups, target):
        results = next(sets_sum_to(self.parsed_data, target, num_groups))
        groups = *results, self.parsed_data.difference(results)
        return min(math.prod(i) for i in groups if
                   len(i) == len(min(groups, key=len)))

    def part_a(self):
        return self.solve(2, sum(self.parsed_data) / 3)

    def part_b(self):
        return self.solve(3, sum(self.parsed_data) / 4)
