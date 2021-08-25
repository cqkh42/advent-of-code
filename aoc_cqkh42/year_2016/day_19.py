from aoc_cqkh42 import BaseSolution


def iteration(nums):
    new = nums[::2]
    if len(nums) % 2:
        new = new[1:]
    return new


class Solution(BaseSolution):
    def part_a(self):
        a = list(range(1, int(self.data) + 1))
        while len(a) > 1:
            a = iteration(a)
        return a[0]

