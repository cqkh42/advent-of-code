from dataclasses import dataclass
import operator
import re

from aoc_cqkh42 import BaseSolution


FUNC_MAP = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    'NOT': lambda _, x: (1 << 16) - 1 - x,
}


@dataclass(init=False)
class Register:
    def __init__(self, instructions):
        register = {}
        for wire_1, op, wire_2, destination in instructions:
            if wire_1.isnumeric():
                wire_1 = int(wire_1)
            if wire_2.isnumeric():
                wire_2 = int(wire_2)

            if not op:
                register[destination] = wire_1
            else:
                register[destination] = (wire_1, FUNC_MAP[op], wire_2)
        self.register = register

    def resolve(self, key):
        value = self[key]
        if isinstance(value, str) and value:
            value = self.resolve(value)
        elif isinstance(value, tuple):
            wire_1, op, wire_2 = value
            value = op(self.resolve(wire_1), self.resolve(wire_2))
        self[key] = value
        return value

    def __getitem__(self, item):
        return self.register.get(item, item)

    def __setitem__(self, key, value):
        self.register[key] = value


class Solution(BaseSolution):
    answer_a = None
    regex = re.compile(r'([a-z0-9]*) ?(\w*) ?([a-z0-9]*) -> (\w+)')

    def parse_data(self):
        return self.regex.findall(self.data)

    def part_a(self):
        register = Register(self.parsed_data)
        self.answer_a = register.resolve('a')
        return self.answer_a

    def part_b(self):
        register = Register(self.parsed_data)
        register['b'] = self.answer_a
        return register.resolve('a')
