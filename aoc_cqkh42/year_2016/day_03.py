import itertools
from dataclasses import dataclass

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Triangle:
    x: int
    y: int
    z: int

    def is_valid(self):
        a = self.x + self.y > self.z
        b = self.x + self.z > self.y
        c = self.y + self.z > self.x
        return a and b and c


def grouper(iterable, n):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


class Solution(BaseSolution):
    def parse_data(self):
        rows = list(parse.findall('{:>d} {:>d} {:>d}', self.data))
        return rows

    def part_a(self):
        triangles = [Triangle(*row) for row in self.parsed_data]
        return sum(triangle.is_valid() for triangle in triangles)

    def part_b(self):
        vertically = itertools.chain.from_iterable(zip(*self.parsed_data))
        triangles = (Triangle(*row) for row in grouper(vertically, 3))
        return sum(triangle.is_valid() for triangle in triangles)
