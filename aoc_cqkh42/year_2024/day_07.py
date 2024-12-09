import math
from typing import Self, Any

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Equation:
    def __init__(self, total, numbers):
        self.total = total
        self.base_total = total
        self.numbers = numbers
        self.base_numbers = [i for i in numbers]
        self.factorise_last()

    def factorise_last(self):
        if not self.numbers:
            return
        if self.total % self.numbers[-1]:
            self.total -= self.numbers.pop(-1)
            self.factorise_last()

    def is_valid(self):
        self.factorise_last()
        if not self.numbers:
            return not self.total

        new_addition = Equation(self.total - self.numbers[-1], self.numbers[:-1])
        new_mul = Equation(self.total // self.numbers[-1], self.numbers[:-1])
        return new_addition.is_valid() or new_mul.is_valid()

    def is_valid_b(self):
        if len(self.numbers) > 1:
            a, b = self.numbers[-2:]
            new_num = int(str(a) + str(b))
            new_equation = Equation(self.total, self.numbers[:-2]+[new_num])
            n = new_equation.is_valid()
        else:
            n = False
        return n

        self.factorise_last()
        if not self.numbers:
            return not self.total

        new_addition = Equation(self.total - self.numbers[-1], self.numbers[:-1])
        new_mul = Equation(self.total // self.numbers[-1], self.numbers[:-1])
        return new_addition.is_valid() or new_mul.is_valid()

    def __repr__(self):
        return f'Equation({self.base_total}, {self.base_numbers})'

class Solution(BaseSolution):
    valid_lines = []
    invalid_lines = []
    PARSER = parse.compile('{:d}')
    def _parse_line(self, line: str):
        left, *right = (result[0] for result in self.PARSER.findall(line))
        e = Equation(left, right)
        return e

    def _parse(self: Self) -> Any:
        valid = []
        invalid = []
        for line in self.parsed_lines:
            if line.is_valid():
                valid.append(line.base_total)
            else:
                invalid.append(Equation(line.base_total, line.base_numbers))
        return valid, invalid

    def part_a(self):
        return sum(self.parsed[0])

    def part_b(self):
        for line in self.parsed[1]:
            print(line, line.is_valid_b())
        return [self.parsed[1]]
        failed = [Equation(line.base_total, line.base_numbers) for line in self.parsed_lines if not line.is_valid()]
        print(failed)
        unfailed = sum([e.base_total for e in failed if not e.is_valid_b()])

        a_sum = sum([line.base_total for line in self.parsed_lines if line.is_valid()])
        return unfailed+a_sum


if __name__ == "__main__":
    submit_answers(Solution,7, 2024)
