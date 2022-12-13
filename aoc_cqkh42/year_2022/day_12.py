from aoc_cqkh42 import BaseSolution

import networkx as nx


class Solution(BaseSolution):
    def parse_data(self):
        graph = nx.grid_2d_graph(len(self.lines[0]), len(self.lines),
                                 create_using=nx.DiGraph)
        to_remove = []
        for (from_x, from_y), (to_x, to_y) in graph.edges(data=False):
            f = self.lines[from_y][from_x]
            t = self.lines[to_y][to_x]
            if f == 'S':
                f = 'a'
            if t == 'E':
                t = 'z'
            if ord(t) - ord(f) <= 1:
                continue
            else:
                to_remove.append(((from_x, from_y), (to_x, to_y)))
        for t in to_remove:
            graph.remove_edge(*t)
        return graph

    def part_a(self):
        for row_index, row in enumerate(self.lines):
            for col_index, val in enumerate(row):
                if val == 'S':
                    start = (col_index, row_index)
                if val == 'E':
                    end = (col_index, row_index)
        return nx.shortest_path_length(self.parsed_data, start, end)

    def part_b(self):
        reversed_graph = self.parsed_data.reverse()
        to_search = []
        for row_index, row in enumerate(self.lines):
            for col_index, val in enumerate(row):
                if val in 'Sa':
                    to_search.append((col_index, row_index))
                if val == 'E':
                    end = (col_index, row_index)
        paths = []
        for start in to_search:
            try:
                length = nx.shortest_path_length(self.parsed_data, start, end)
            except nx.NetworkXNoPath:
                continue
            else:
                paths.append(length)
        return min(paths)