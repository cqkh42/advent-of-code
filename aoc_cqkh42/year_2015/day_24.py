# TODO really messy
import functools
import itertools
import math

from aoc_cqkh42 import BaseSolution


@functools.cache
def subsets_equal_to(set_, target):
    s = sorted(set_)
    for size in range(1, len(s)+1):
        if sum(s[:size]) <= target <= sum(s[-size:]):
            combs = itertools.combinations(set_, size)
            yield (comb for comb in combs if sum(comb) == target)


class Solution(BaseSolution):
    def parse_data(self):
        parcels = [int(i) for i in self.lines]
        return frozenset(parcels)

    def part_a(self):
        packages = self.parsed_data
        group_weight = sum(self.parsed_data) / 3

        possible_first_groups = (subsets_equal_to(packages,
                                                 group_weight))

        for size in possible_first_groups:
            results = []
            for group in size:
                others = packages.difference()
                if subsets_equal_to(others, group_weight):
                    results.append(math.prod(group))
            if results:
                return min(results)

    def part_b(self):
        packages = self.parsed_data
        total_weight = sum(packages)
        group_weight = total_weight / 4
        possible_first_groups = subsets_equal_to(packages,
                                                 group_weight)
        #
        for size in possible_first_groups:
            results = []
            for group in size:
                others = packages.difference()
                if (
                bits := subsets_equal_to(others, group_weight)):
                    for _ in bits:
                        k = others.difference(bits)
                        if subsets_equal_to(k, group_weight):
                            results.append(math.prod(group))
            if results:
                return min(results)
