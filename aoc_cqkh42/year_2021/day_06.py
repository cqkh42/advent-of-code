from collections import defaultdict

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        numbers = [int(num) for num in self.input_.split(',')]
        tracker = defaultdict(int)
        for num in numbers:
            tracker[num] += 1
        return tracker

    def part_a(self):
        for day in range(80):
            temp = self.parsed.copy()
            self.parsed[8] = temp[0]
            self.parsed[7] = temp[8]
            self.parsed[6] = temp[0] + temp[7]
            self.parsed[5] = temp[6]
            self.parsed[4] = temp[5]
            self.parsed[3] = temp[4]
            self.parsed[2] = temp[3]
            self.parsed[1] = temp[2]
            self.parsed[0] = temp[1]
        return sum(self.parsed.values())

    def part_b(self):
        for day in range(176):
            temp = self.parsed.copy()
            self.parsed[8] = temp[0]
            self.parsed[7] = temp[8]
            self.parsed[6] = temp[0] + temp[7]
            self.parsed[5] = temp[6]
            self.parsed[4] = temp[5]
            self.parsed[3] = temp[4]
            self.parsed[2] = temp[3]
            self.parsed[1] = temp[2]
            self.parsed[0] = temp[1]
        return sum(self.parsed.values())
