import itertools
from collections import defaultdict
from typing import Self, Any

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.coords import Coords


def _find_single_antinodes(a: Coords, b: Coords):
    x_diff = abs(a.x - b.x) ## how far to the right x is
    y_diff = abs(a.y - b.y)

    if a.x > b.x: # a is further to the right
        x_1 = a.x + x_diff
        x_2 = b.x - x_diff
    else:
        x_1 = a.x - x_diff
        x_2 = b.x + x_diff

    if a.y > b.y:
        y_1 = a.y + y_diff
        y_2 = b.y - y_diff
    else:
        y_1 = a.y - y_diff
        y_2 = b.y + y_diff

    return Coords(x_1, y_1), Coords(x_2, y_2)

def find_antinodes(locations):
    nodes = more_itertools.flatten(_find_single_antinodes(a, b) for a, b in itertools.combinations(locations, 2))
    return list(nodes)



class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        vals = defaultdict(set)

        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                if value != '.':
                    vals[value].add(Coords(x_index, y_index))
        return vals

    def part_a(self):
        a = set()
        for k, values in self.parsed.items():
            v = find_antinodes(values)
            a.update(v)
        a = {i for i in a if 0 <=i.x < len(self.lines[0]) and 0<=i.y < self.num_lines }
        return len(a)

    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,8, 2024)
