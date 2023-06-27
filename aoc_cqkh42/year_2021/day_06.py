from collections import defaultdict

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        numbers = [int(num) for num in self.data.split(',')]
        tracker = defaultdict(int)
        for num in numbers:
            tracker[num] += 1
        return tracker

    def part_a(self):
        for day in range(80):
            temp = self.parsed_data.copy()
            self.parsed_data[8] = temp[0]
            self.parsed_data[7] = temp[8]
            self.parsed_data[6] = temp[0] + temp[7]
            self.parsed_data[5] = temp[6]
            self.parsed_data[4] = temp[5]
            self.parsed_data[3] = temp[4]
            self.parsed_data[2] = temp[3]
            self.parsed_data[1] = temp[2]
            self.parsed_data[0] = temp[1]
        return sum(self.parsed_data.values())

    def part_b(self):
        for day in range(176):
            temp = self.parsed_data.copy()
            self.parsed_data[8] = temp[0]
            self.parsed_data[7] = temp[8]
            self.parsed_data[6] = temp[0] + temp[7]
            self.parsed_data[5] = temp[6]
            self.parsed_data[4] = temp[5]
            self.parsed_data[3] = temp[4]
            self.parsed_data[2] = temp[3]
            self.parsed_data[1] = temp[2]
            self.parsed_data[0] = temp[1]
        return sum(self.parsed_data.values())
