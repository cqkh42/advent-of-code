from collections import Counter

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        horizontal = []
        vertical = []
        diagonal = []
        parser = parse.compile(r'{:d},{:d} -> {:d},{:d}')
        for x1, y1, x2, y2 in parser.findall(self.data):
            if x1 == x2:
                # horizontal line
                start, end = sorted([y1, y2])
                l = [(x1, y) for y in range(start, end+1)]
                horizontal.extend(l)
            elif y1 == y2:
                # vertical line
                start, end = sorted([x1, x2])
                l = [(x, y1) for x in range(start, end+1)]
                vertical.extend(l)
            elif x1 < x2:
                x_range = range(x1, x2+1)
                y_range = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
                l = [(x, y) for x, y in
                     zip(x_range, y_range)]
                diagonal.extend(l)
            else:
                x_range = range(x1, x2-1, -1)
                y_range = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
                l = [(x, y) for x, y in
                     zip(x_range, y_range)]
                diagonal.extend(l)
        return horizontal + vertical, diagonal

    def part_a(self):
        c = Counter(self.parsed_data[0])
        return sum(count > 1 for count in c.values())

    def part_b(self):
        c = Counter(self.parsed_data[0] + self.parsed_data[1])
        return sum(count > 1 for count in c.values())
