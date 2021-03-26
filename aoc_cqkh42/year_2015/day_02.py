from dataclasses import dataclass
import itertools
import math
from typing import List

import parse

from aoc_cqkh42 import BaseSolution


@dataclass
class Present:
    dims: List[int]

    def sides(self):
        return itertools.combinations(self.dims, 2)

    def paper(self):
        sides = [math.prod(corner) for corner in self.sides()]
        return min(sides) + sum(sides)*2

    def ribbon(self):
        perms = (sum(corner) for corner in self.sides())
        return min(perms)*2 + math.prod(self.dims)


class Solution(BaseSolution):
    parser = parse.compile('{:d}x{:d}x{:d}')

    def parse_data(self):
        presents = [Present(dims) for dims in self.parser.findall(self.data)]
        return presents

    def part_a(self):
        return sum(present.paper() for present in self.parsed_data)

    def part_b(self):
        return sum(present.ribbon() for present in self.parsed_data)
