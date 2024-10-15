import itertools

import functools
import itertools
from dataclasses import dataclass

@dataclass
class Program:
    name: str
    weight: int
    dependencies: list[str]

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

class Solution(BaseSolution):

    def part_a(self):

        holding = [row for row in self.input_.split('\n') if '->' in row]
        lefts = {row.split()[0] for row in holding}
        rights = (row.split('-> ')[1] for row in holding)
        rights = [row.split(', ') for row in rights]
        rights = set(itertools.chain.from_iterable(rights))
        return lefts.difference(rights).pop()


    def part_b(data, **_):
        return False


if __name__ == "__main__":
    submit_answers(Solution, 7, 2017)
