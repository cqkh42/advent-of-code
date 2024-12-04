import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        return sum(
            second > line
            for (line, second) in more_itertools.pairwise(self.numbers)
        )

    def part_b(self):
        windows = (
            sum(nums) for nums in more_itertools.triplewise(self.numbers)
        )
        return sum(
            second > line
            for (line, second) in more_itertools.pairwise(windows)
        )
