# TODO really messy
import itertools
import math

from aoc_cqkh42 import BaseSolution


def subsets_equal_to(set_, target):
    for size in range(1, len(set_)+1):
        combs = itertools.combinations(set_, size)
        yield (comb for comb in combs if sum(comb) == target)


class Solution(BaseSolution):
    def parse_data(self):
        return frozenset(self.numbers)

    def part_a(self):
        for size in range(len(self.parsed_data)):
            combs = (
                math.prod(comb)
                for comb in itertools.combinations(self.parsed_data, size)
                if sum(comb) == sum(self.parsed_data) / 3
            )
            try:
                return min(combs)
            except ValueError:
                continue

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
