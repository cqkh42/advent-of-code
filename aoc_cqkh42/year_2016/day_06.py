from collections import Counter

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        rows = self.data.split('\n')
        cols = zip(*rows)
        counters = [Counter(col) for col in cols]
        return counters

    def part_a(self):
        a = [col.most_common(1)[0][0] for col in self.parsed_data]
        return ''.join(a)

    def part_b(self):
        a = [col.most_common()[-1][0] for col in self.parsed_data]
        return ''.join(a)
