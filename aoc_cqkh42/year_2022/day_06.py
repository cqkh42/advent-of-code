from aoc_cqkh42 import BaseSolution

import more_itertools


class Solution(BaseSolution):
    def solve(self, size):
        for index in range(len(self.data)):
            if more_itertools.all_unique(self.data[index:index+size]):
                return index+size

    def part_a(self):
        return self.solve(4)

    def part_b(self):
        return self.solve(14)
