import functools
from typing import Self, Any

import more_itertools
import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2017.day_10 import KnotHash


@functools.cache
def process_line(input_):
    hasher = KnotHash(input_)
    hashed = hasher.make_hash()
    bytes = ''.join(hex_to_bytes(char) for char in hashed)
    return bytes

def hex_to_bytes(char):
    num = f'{int(char, 16):b}'
    return f'{num:0>4}'

class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        a = [self.input_ + f'-{num}' for num in range(128)]
        b = [process_line(line) for line in a]
        return b

    def part_a(self, size=256):
        return sum(line.count('1') for line in self.processed)

    def part_b(self):
        g = nx.grid_graph((128, 128))
        pairs = []
        for x in range(128):
            for y in range(128):
                if self.processed[x][y] != '1':
                    pairs.append((x, y))
        g.remove_nodes_from(pairs)
        return more_itertools.ilen(nx.connected_components(g))


if __name__ == "__main__":
    submit_answers(Solution, 14, 2017)