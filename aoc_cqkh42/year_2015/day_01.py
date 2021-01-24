import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        return self.data.count('(') - self.data.count(')')

    def part_b(self):
        instructions = (1 if item == '(' else -1 for item in self.data)
        return list(itertools.accumulate(instructions)).index(-1) + 1
