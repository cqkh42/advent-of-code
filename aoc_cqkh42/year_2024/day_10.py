from itertools import product
from typing import Self, Any

import more_itertools
import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    heights = None
    zeros = None

    def grid(self):
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                yield (x_index, y_index), int(value)

    def _parse(self: Self) -> Any:
        g = nx.DiGraph()
        heights = {}
        for (x, y), value in self.grid():
                heights[(x, y)] = value
                for x_delta, y_delta in (0,1), (0,-1), (1, 0), (-1, 0):
                    try:
                        other_node = self.lines[y+y_delta][x+x_delta]

                        if value + 1 == int(other_node):
                            g.add_edge((x, y), (x+x_delta, y+y_delta))
                    except IndexError:
                        continue
        self.heights = heights

        zeros = [k for k in self.heights if self.heights[k] == 0]
        nines = [k for k in self.heights if self.heights[k] == 9]

        return [more_itertools.ilen(nx.all_simple_paths(g, start, end)) for start, end in product(zeros, nines)]


    def part_a(self):
        return sum(paths > 0 for paths in self.parsed)

    def part_b(self):
        return sum(self.parsed)


if __name__ == "__main__":
    submit_answers(Solution,10, 2024)
