import more_itertools
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile('{:d},{:d}')
    y_break = float('inf')

    def parse_data(self) -> set:
        rocks = set()
        for row in self.lines:
            for (start_x, start_y), (end_x, end_y) in more_itertools.pairwise(
                    self.parser.findall(row)):
                if start_x == end_x:
                    start, end = sorted([start_y, end_y])
                    for y in range(start, end + 1):
                        rocks.add((start_x, y))
                elif start_y == end_y:
                    start, end = sorted([start_x, end_x])
                    for x in range(start, end + 1):
                        rocks.add((x, start_y))
        self.y_break = max(y for x, y in rocks)
        return rocks

    def drop_grain(self, sand):
        busy = self.parsed_data.union(sand)
        x, y = 500, 0
        while True:
            if y > self.y_break:
                raise ValueError
            if (x, y+1) not in busy:
                y += 1
            elif (x-1, y+1) not in busy:
                x -= 1
                y += 1
            elif (x+1, y+1) not in busy:
                x += 1
                y += 1
            else:
                return x, y

    def drop_grain_b(self, sand):
        busy = self.parsed_data.union(sand)
        x, y = 500, 0
        while True:
            if (x, y+1) not in busy:
                y += 1
            elif (x-1, y+1) not in busy:
                x -= 1
                y += 1
            elif (x+1, y+1) not in busy:
                x += 1
                y += 1
            else:
                return x, y

    def part_a(self):
        count = 0
        sand_pile = set()
        while True:
            try:
                sand_pile.add(self.drop_grain(sand_pile))
                count += 1
            except ValueError:
                return count

    def part_b(self):
        to_add = {(x, self.y_break+2) for x in range(1001)}
        self.parsed_data = self.parsed_data.union(to_add)
        count = 0
        sand_pile = set()
        while True:
            new = self.drop_grain_b(sand_pile)
            sand_pile.add(new)
            count += 1
            if new == (500, 0):
                return count

