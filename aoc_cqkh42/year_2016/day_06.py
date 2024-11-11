from collections import Counter

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self):
        cols = zip(*self.lines)
        counters = [Counter(col) for col in cols]
        return [counter.most_common() for counter in counters]

    def part_a(self):
        a = [col[0][0] for col in self.processed]
        return "".join(a)

    def part_b(self):
        a = [col[-1][0] for col in self.processed]
        return "".join(a)
