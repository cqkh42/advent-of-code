import itertools
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    heights = None
    def _parse(self: Self) -> Any:
        g = nx.DiGraph()
        heights = {}
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                heights[(x_index, y_index)] = int(value)
                for x_delta, y_delta in (0,1), (0,-1), (1, 0), (-1, 0):
                    try:
                        other_node = self.lines[y_index+y_delta][x_index+x_delta]

                        if int(value) + 1 == int(other_node):
                            g.add_edge((x_index, y_index), (x_index+x_delta, y_index+y_delta))
                    except IndexError:
                        continue
        self.heights = heights
        return g


    def part_a(self):
        zeros = [k for k in self.heights if self.heights[k] == 0]
        nines = [k for k in self.heights if self.heights[k] == 9]

        total = 0
        for start, end in itertools.product(zeros, nines):
            if nx.has_path(self.parsed, start, end):
                total += 1
        return total

    def part_b(self):
        zeros = [k for k in self.heights if self.heights[k] == 0]
        nines = [k for k in self.heights if self.heights[k] == 9]

        total = 0
        for start, end in itertools.product(zeros, nines):
            a = list(nx.all_simple_paths(self.parsed, start, end))
            total += len(a)
        return total


if __name__ == "__main__":
    submit_answers(Solution,10, 2024)
