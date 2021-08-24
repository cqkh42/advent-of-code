# TODO use parse here
# TODO and recursion
from dataclasses import dataclass
import operator
import re

from aoc_cqkh42 import BaseSolution


@dataclass
class Register:
    def __init__(self, register, instructions):
        self.register = register
        self.instructions = instructions

    func_map = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        'NOT': lambda _, x: (1 << 16) - 1 - x,
        '': lambda x, _: x
    }

    def get(self, obj):
        return self.register.get(obj)

    def parse_input(self, signal):
        if signal.isnumeric():
            return int(signal)
        else:
            return self.get(signal)

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def solve_equation(self, wire_1, gate, wire_2):
        wire_1 = self.parse_input(wire_1)
        wire_2 = self.parse_input(wire_2)
        op = self.func_map[gate]
        result = op(wire_1, wire_2)

        if result is None:
            raise ValueError
        return result


def _assemble_wires(instructions):

    t = {destination: (wire_1, op, wire_2) for wire_1, op, wire_2, destination in instructions}
    register = Register({}, instructions)

    for wire_1, op, wire_2, destination in register.instructions:
        try:
            value = register.solve_equation(wire_1, op, wire_2)
        except (TypeError, ValueError):
            register.add_instruction((wire_1, op, wire_2, destination))
        else:
            register.register[destination] = value
    return register.register


class Solution(BaseSolution):
    answer_a = None
    regex = re.compile(r'([a-z0-9]*) ?([A-Z]*) ?([a-z0-9]*) -> ([a-z0-9]+)')

    def parse_data(self):
        return self.regex.findall(self.data)

    def part_a(self):
        register = _assemble_wires(self.parsed_data)
        self.answer_a = register['a']
        return register['a']

    def part_b(self):
        b_set_at = [output for *_, output in self.parsed_data].index('b')
        self.parsed_data[b_set_at] = (str(self.answer_a), '', '', 'b')
        register = _assemble_wires(self.parsed_data)
        return register['a']
