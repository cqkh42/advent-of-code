import numpy as np

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return np.array([list(line) for line in self.lines]).astype(int)

    def part_a(self):
        gamma = self.parsed_data.mean(axis=0).round().astype(int).astype(str)
        gamma = ''.join(gamma)
        epsilon = ''.join('1' if num == '0' else '0' for num in gamma)
        return int(gamma, 2) * int(epsilon, 2)

    def _oxygen(self):
        data = self.parsed_data
        for column in range(self.parsed_data.shape[1]):
            target = 1 if data[:, column].mean() >= 0.5 else 0
            data = data[data[:, column] == target]
            if len(data) == 1:
                a = ''.join(data[0].astype(str))
                return int(a, 2)

    def _co2(self):
        data = self.parsed_data
        for column in range(self.parsed_data.shape[1]):
            target = 0 if data[:, column].mean() >= 0.5 else 1
            data = data[data[:, column] == target]
            if len(data) == 1:
                a = ''.join(data[0].astype(str))
                return int(a, 2)

    def part_b(self):
        oxygen = self._oxygen()
        co2 = self._co2()
        return oxygen * co2
