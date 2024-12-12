from collections import Counter
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    def _parse(self: Self) -> tuple[list[int, ...], list[int, ...]]:
        return sorted(self.numbers[::2]), sorted(self.numbers[1::2])

    def part_a(self):
        return sum(abs(left - right) for left, right in zip(*self.parsed))

    def part_b(self):
        counted = Counter(self.parsed[1])
        return sum(left*counted[left] for left in self.parsed[0])

if __name__ == "__main__":
    submit_answers(Solution, 1, 2024)
