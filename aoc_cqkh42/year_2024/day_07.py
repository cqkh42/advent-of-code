import itertools
from typing import Self, Any

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Equation:
    PARSER = parse.compile('{:d}')
    def __init__(self, data):
        if isinstance(data, str):
            total, *numbers = (result[0] for result in self.PARSER.findall(data))
        else:
            total, *numbers = data
        self.total = total
        self.base_total = total
        self.numbers = numbers
        self.base_numbers = [i for i in numbers]

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

        new_addition = Equation([self.total - self.numbers[-1], *self.numbers[:-1]])
        new_mul = Equation([self.total // self.numbers[-1], *self.numbers[:-1]])
        return new_addition.is_valid() or new_mul.is_valid()

    def is_valid_b(self):
        num_indices = len(self.numbers) - 1
        options = ['add', 'concat', 'mul']
        paths = itertools.product(options, repeat=num_indices)

        for path in paths:
            start = self.numbers[0]
            for num, operator in zip(self.numbers[1:], path):
                if operator == 'add':
                    start += num
                elif operator == 'mul':
                    start *= num
                else:
                    start = int(str(start) + str(num))
            if start == self.base_total:
                return True
        return False

    def __repr__(self):
        return f'Equation({self.base_total}, {self.base_numbers})'

class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        valid = []
        invalid = []
        for line in self.lines_as(Equation):
            if line.is_valid():
                valid.append(line.base_total)
            else:
                invalid.append(Equation([line.base_total, *line.base_numbers]))
        return valid, invalid

    def part_a(self):
        return sum(self.parsed[0])

    def part_b(self):
        new = sum(equation.base_total for equation in self.parsed[1] if equation.is_valid_b())
        return sum(self.parsed[0]) + new


if __name__ == "__main__":
    submit_answers(Solution,7, 2024)
