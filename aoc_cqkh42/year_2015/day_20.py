import numpy as np

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return int(self.data)

    n = 1000000

    def part_a(self):
        houses = np.ones(self.n)
        houses *= 10
        for elf in range(2, self.n):
            houses[elf::elf] += (elf * 10)
        return np.argmax(houses > self.parsed_data)

    def part_b(self):
        houses = np.ones(self.n)
        houses *= 11
        for elf in range(2, self.n):
            houses[elf:(elf*50)+1:elf] += (elf * 11)
        return np.argmax(houses > self.parsed_data)
