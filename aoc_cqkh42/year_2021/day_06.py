from collections import defaultdict

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self):
        numbers = [int(num) for num in self.input_.split(',')]
        tracker = defaultdict(int)
        for num in numbers:
            tracker[num] += 1
        return tracker

    def part_a(self):
        for day in range(80):
            temp = self.processed.copy()
            self.processed[8] = temp[0]
            self.processed[7] = temp[8]
            self.processed[6] = temp[0] + temp[7]
            self.processed[5] = temp[6]
            self.processed[4] = temp[5]
            self.processed[3] = temp[4]
            self.processed[2] = temp[3]
            self.processed[1] = temp[2]
            self.processed[0] = temp[1]
        return sum(self.processed.values())

    def part_b(self):
        for day in range(176):
            temp = self.processed.copy()
            self.processed[8] = temp[0]
            self.processed[7] = temp[8]
            self.processed[6] = temp[0] + temp[7]
            self.processed[5] = temp[6]
            self.processed[4] = temp[5]
            self.processed[3] = temp[4]
            self.processed[2] = temp[3]
            self.processed[1] = temp[2]
            self.processed[0] = temp[1]
        return sum(self.processed.values())
