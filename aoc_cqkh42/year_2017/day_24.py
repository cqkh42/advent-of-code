from collections import defaultdict
from functools import cached_property
from typing import Self, Any

from more_itertools import flatten
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo line numbers
class Solution(BaseSolution):
    maps = defaultdict(set)
    def _parse_line(self, line: str):
        a= tuple([int(i) for i in line.split('/')])
        self.maps[a[0]].add(a)
        self.maps[a[1]].add(a)

    def _parse(self: Self) -> Any:
        return frozenset(self.parsed_lines)

    def neighbours(self, visited):
        if len(visited) == 1:
            v = max({i for i in visited[-1] if i != 0})
            left = self.maps[v]
            # right = self.maps[visited[-1][1]]
            options = left.difference(visited)
        elif visited[-1][0] in visited[-2]:
            options = self.maps[visited[-1][1]].difference(visited)
        else:
            options = self.maps[visited[-1][0]].difference(visited)
        return [tuple([*visited, option]) for option in options]

    @cached_property
    def term(self):
        term = []
        queue = [[i] for i in self.maps[0]]
        while queue:
            node = queue.pop()
            neighbors = self.neighbours(node)
            if not neighbors:
                term.append(node)
            else:
                queue.extend(neighbors)
        return term

    def part_a(self):
        t = [sum(flatten(te)) for te in self.term]
        return max(t)

    def part_b(self):
        l = max(len(i) for i in self.term)
        term = [i for i in self.term if len(i) == l]
        t = [sum(flatten(te)) for te in term]
        return max(t)



if __name__ == "__main__":
    submit_answers(Solution,24, 2017)
