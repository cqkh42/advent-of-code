import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        parser = parse.compile("{:d}-{:d}")
        rs = parser.findall(self.input_)
        rs = sorted([(a, b) for a, b in rs], key=lambda x: x[0])
        ranges = []

        current = list(rs[0])

        for start, end in rs:
            if start <= current[1] + 1:
                current[1] = max(end, current[1])
            else:
                ranges.append(current)
                current = [start, end]
        ranges.append(current)
        ranges = [range(a, b + 1) for a, b in ranges]
        return ranges

    def part_a(self):
        first_range = self.parsed[0]
        return max(first_range) + 1

    def part_b(self):
        bad_count = sum(len(i) for i in self.parsed)
        return 4294967295 + 1 - bad_count
