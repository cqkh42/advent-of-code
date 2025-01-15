from functools import cached_property
from typing import Self, Any

import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra_path_length, \
    single_source_dijkstra_path_length

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    start = None
    end = None
    scores = {}
    def _parse(self: Self) -> Any:
        graph = nx.Graph()
        for y, row in enumerate(self.lines):
            for x, val in enumerate(row):
                if val == 'S':
                    graph.add_edge('START', (x, y, 'E'), weight=0)
                elif val == 'E':
                    for direction in 'NSWE':
                        graph.add_edge((x, y, direction), 'END', weight=0)
                if val == '#':
                    continue
                # look up
                if self.lines[y - 1][x] != '#':
                    graph.add_edge((x, y, 'N'),
                                   (x, y - 1, 'N'), weight=1)
                # look down
                if self.lines[y + 1][x] != '#':
                    graph.add_edge((x, y, 'S'),
                                   (x, y + 1, 'S'), weight=1)
                # look left
                if self.lines[y][x - 1] != '#':
                    graph.add_edge((x, y, 'W'),
                                   (x - 1, y, 'W'), weight=1)
                # look right
                if self.lines[y][x + 1] != '#':
                    graph.add_edge((x, y, 'E'),
                                   (x + 1, y, 'E'), weight=1)
                # add turns
                for l, r in ['NE', 'ES', 'SW', 'WN']:
                    graph.add_edge((x, y, l),
                                   (x, y, r), weight=1000)
        return graph

    @cached_property
    def best_score(self):
        return dijkstra_path_length(self.parsed, 'START', 'END')

    def part_a(self):
        return self.best_score

    def part_b(self):
        from_start = single_source_dijkstra_path_length(self.parsed, cutoff=self.best_score, source='START')
        from_end = single_source_dijkstra_path_length(self.parsed, cutoff=self.best_score, source='END')
        totals = {
            node[:2] for node in from_start
            if node in from_end
               and node not in ['START', 'END']
               and from_start[node] + from_end[node] == self.best_score

        }
        return len(totals)

if __name__ == "__main__":
    submit_answers(Solution,16, 2024)
