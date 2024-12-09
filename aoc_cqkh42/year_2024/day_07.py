import math

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Equation:
    def __init__(self, total, numbers):
        self.total = total
        self.base_total = total
        self.numbers = numbers
        self.factorise_last()

    def factorise_last(self):
        if not self.numbers:
            return
        if self.total % self.numbers[-1]:
            self.total -= self.numbers.pop(-1)
            self.factorise_last()

    def is_valid(self):
        if not self.numbers and not self.total:
            return True
        elif not self.numbers and self.total:
            return False
        if self.total < 0:
            return False
        if sum(self.numbers) == self.total:
            return True
        if not self.numbers:
            return False

        new_addition = Equation(self.total - self.numbers[-1], [i for i in self.numbers[:-1]])
        new_mul = Equation(self.total // self.numbers[-1], [i for i in self.numbers[:-1]])
        return new_addition.is_valid() or new_mul.is_valid()

    def __repr__(self):
        return f'Equation({self.total}, {self.numbers})'

class Solution(BaseSolution):
    PARSER = parse.compile('{:d}')
    def _parse_line(self, line: str):
        left, *right = (result[0] for result in self.PARSER.findall(line))
        e = Equation(left, right)
        return e

    def part_a(self):
        # for line, base in zip(self.parsed_lines, self.lines):
        #     if not line.is_valid():
        #         print(line.base_total, base)
        return sum([line.base_total for line in self.parsed_lines if line.is_valid()])

    def part_b(self):
        ...

if __name__ == "__main__":
    submit_answers(Solution,7, 2024)
