from aoc_cqkh42 import BaseSolution

import parse


class Solution(BaseSolution):
    parser = parse.compile('{:d}-{:d},{:d}-{:d}')

    def parse_data(self):
        return [
            (set(range(a, b+1)), set(range(c, d+1)))
            for a, b, c, d in self.parser.findall(self.data)
        ]

    def part_a(self):
        return sum(r.issubset(l) or l.issubset(r)for l, r in self.parsed_data)

    def part_b(self):
        return sum(bool(r.intersection(l)) for l, r in self.parsed_data)
