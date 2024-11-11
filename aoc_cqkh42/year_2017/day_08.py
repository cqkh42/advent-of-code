import operator
from collections import defaultdict
from typing import Self

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    highest_seen = 0
    def _process_data(self: Self):
        mappings = {
            'inc': operator.add,
            'dec': operator.sub,
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '==': operator.eq,
            '<=': operator.le,
            '!=': operator.ne
        }
        parser = parse.compile('{:l} {:l} {:d} if {:l} {} {:d}')
        results = []
        for modify, instruction, amount, predicate, condition, value in parser.findall(self.input_):
            results.append((modify, mappings[instruction], amount, predicate, mappings[condition], value))
        return results


    def part_a(self):
        registers = defaultdict(int)
        for modify, instruction, amount, predicate, condition, value in self.processed:
            if condition(registers[predicate], value):
                new_value = instruction(registers[modify], amount)
                self.highest_seen = max(self.highest_seen, new_value)
                registers[modify] = new_value
        return max(registers.values())

    def part_b(self):
        return self.highest_seen

if __name__ == "__main__":
    submit_answers(Solution, 8, 2017)
