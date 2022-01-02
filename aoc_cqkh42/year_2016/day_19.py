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

    def part_b(self):
        # Find the base before
        one_wins_at = [4, 10, 28]

        while True:
            last, current = one_wins_at[-2:]
            next_ = 4 * current - 3 * last
            one_wins_at.append(next_)
            if next_ > int(self.data):
                break
        start, end = one_wins_at[-2:]

        inflection = ((start + end) / 2) - 1
        if int(self.data) <= inflection:
            return int(self.data) - start + 1
        else:
            raise NotImplementedError
            # this actually now incrememnts by two