import itertools
import math
from dataclasses import dataclass
from typing import List

import parse

from aoc_cqkh42 import BaseSolution


@dataclass
class Present:
    dims: List[int]

    @property
    def sides(self) -> itertools.combinations:
        return itertools.combinations(self.dims, 2)

    @property
    def paper(self) -> int:
        sides = [math.prod(corner) for corner in self.sides]
        return min(sides) + sum(sides) * 2

    @property
    def ribbon(self) -> int:
        perms = (sum(corner) for corner in self.sides)
        return min(perms) * 2 + math.prod(self.dims)


class Solution(BaseSolution):
    parser = parse.compile("{:d}x{:d}x{:d}")

    def parse_data(self) -> List[Present]:
        presents = [Present(dims) for dims in self.parser.findall(self.data)]
        return presents

    def part_a(self) -> int:
        return sum(present.paper for present in self.parsed_data)

    def part_b(self) -> int:
        return sum(present.ribbon for present in self.parsed_data)
