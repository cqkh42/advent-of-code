import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile('{:d}-{:d},{:d}-{:d}')

    def parse_data(self):
        return [
            (set(range(a, b + 1)), set(range(c, d + 1)))
            for a, b, c, d in self.parser.findall(self.data)
        ]

    def part_a(self):
        return sum(
            right.issubset(left) or left.issubset(right)
            for left, right in self.parsed_data
        )

    def part_b(self):
        return sum(
            bool(right.intersection(left))
            for left, right in self.parsed_data
        )
