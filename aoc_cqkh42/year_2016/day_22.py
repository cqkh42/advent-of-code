import itertools
from dataclasses import dataclass

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile(
    r'/dev/grid/node-x{test[x]:d}-y{test[y]:d}{:s}{test[size]:d}T{:s}{test[used]:d}T{:s}{test[avail]:d}T'
)


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    size: int
    used: int
    avail: int


class Solution(BaseSolution):
    def _process_data(self):
        rows = list(PARSER.findall(self.input_))
        nodes = [Node(**row.named['test']) for row in rows]
        return nodes

    def part_a(self):
        viable = set()
        for node_a, node_b in itertools.permutations(self.processed, 2):
            if node_a.used and node_a.used <= node_b.avail:
                s = frozenset((node_a, node_b))
                viable.add(s)
        return len(viable)
