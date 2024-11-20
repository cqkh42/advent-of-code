import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        return int(self.input_)

    n = 1000000

    def part_a(self):
        houses = np.ones(self.n)
        houses *= 10
        for elf in range(2, self.n):
            houses[elf::elf] += elf * 10
        return str(np.argmax(houses > self.parsed))

    def part_b(self):
        houses = np.ones(self.n)
        houses *= 11
        for elf in range(2, self.n):
            houses[elf : (elf * 50) + 1 : elf] += elf * 11
        return str(np.argmax(houses > self.parsed))


if __name__ == "__main__":
    submit_answers(Solution, 20, 2015)
