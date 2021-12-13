from collections import Counter
from dataclasses import dataclass
import itertools

from aoc_cqkh42 import BaseSolution


@dataclass
class Puzzle:
    left: list[set[str]]
    right: list[set[str]]

    numbers = (
        frozenset({0, 1, 3, 4, 5, 6}),  # 0
        frozenset({3, 6}),  # 1
        frozenset({0, 2, 3, 4, 5}),  # 2
        frozenset({0, 3, 2, 6, 5}),  # 3
        frozenset({1, 3, 2, 6}),  # 4
        frozenset({0, 1, 2, 5, 6}),  # 5
        frozenset({0, 1, 2, 4, 5, 6}),  # 6
        frozenset({0, 3, 6}),  # 7
        frozenset({0, 1, 2, 3, 4, 5, 6}),  # 8
        frozenset({0, 1, 2, 3, 5, 6})  # 9
    )

    def solve(self):
        combs = itertools.permutations('abcdefg')
        for comb in combs:
            f = {
                frozenset([comb.index(char) for char in number])
                for number in self.left
            }
            if f == set(self.numbers):
                print(f)
                final = (
                    frozenset([comb.index(char) for char in number])
                    for number in self.right
                )
                final = int(''.join(str(self.numbers.index(i)) for i in final))
                return final

    @classmethod
    def from_line(cls, line):
        left, right = line.split('|')
        left = [set(i) for i in left.split()]
        right = [set(i) for i in right.split()]
        return Puzzle(left, right)


class Solution(BaseSolution):
    def parse_data(self):
        return [Puzzle.from_line(line) for line in self.lines]

    def part_a(self):
        good_sizes = {2, 3, 4, 7}
        a = [
            sum(len(part) in good_sizes for part in puzzle.right)
            for puzzle in self.parsed_data
        ]
        return sum(a)

    def part_b(self):
        return sum(puzzle.solve() for puzzle in self.parsed_data)
