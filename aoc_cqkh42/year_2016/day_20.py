import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    LINE_PARSER = parse.compile("{:d}-{:d}")

    def _parse_line(self, line: str):
        found = self.LINE_PARSER.search(line)
        return found[0], found[1]

    def _parse(self):
        rs = sorted(self.parsed_lines)
        ranges = []

        current = list(rs[0])

        for start, end in rs:
            if start <= current[1] + 1:
                current[1] = max(end, current[1])
            else:
                ranges.append(current)
                current = [start, end]
        ranges.append(current)
        return [range(a, b + 1) for a, b in ranges]

    def part_a(self):
        first_range = self.parsed[0]
        return max(first_range) + 1

    def part_b(self):
        bad_count = sum(len(i) for i in self.parsed)
        return 4294967295 + 1 - bad_count
