import itertools
from dataclasses import dataclass

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Puzzle:
    left: list[set[str]]
    right: list[set[str]]

    numbers = {
        frozenset({0, 1, 3, 4, 5, 6}) : '0',  # 0
        frozenset({3, 6}): '1',  # 1
        frozenset({0, 2, 3, 4, 5}): '2',  # 2
        frozenset({0, 3, 2, 6, 5}): '3',  # 3
        frozenset({1, 3, 2, 6}): '4',  # 4
        frozenset({0, 1, 2, 5, 6}): '5',  # 5
        frozenset({0, 1, 2, 4, 5, 6}): '6',  # 6
        frozenset({0, 3, 6}): '7',  # 7
        frozenset({0, 1, 2, 3, 4, 5, 6}): '8',  # 8
        frozenset({0, 1, 2, 3, 5, 6}): '9'  # 9
    }

    def do_iter(self, comb):
        for number in self.left:
            z = frozenset({comb.index(char) for char in number})
            if z not in self.numbers:
                break
        else:
            final = (
                frozenset([comb.index(char) for char in number])
                for number in self.right
            )
            final = int(''.join(self.numbers[i] for i in final))
            return final

    def solve(self):
        combs = itertools.permutations('abcdefg')
        for comb in combs:
            if z := self.do_iter(comb):
                return z


    @classmethod
    def from_line(cls, line):
        left, right = line.split('|')
        left = [set(i) for i in left.split()]
        right = [set(i) for i in right.split()]
        return Puzzle(left, right)


class Solution(BaseSolution):
    def _process_data(self):
        return [Puzzle.from_line(line) for line in self.lines]

    def part_a(self):
        good_sizes = {2, 3, 4, 7}
        a = [
            sum(len(part) in good_sizes for part in puzzle.right)
            for puzzle in self.processed
        ]
        return sum(a)

    def part_b(self):
        return sum(puzzle._solve() for puzzle in self.processed)
