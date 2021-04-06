# TODO use parse here

import operator
import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    answer_a = None
    regex = re.compile(r'([a-z0-9]*) ?([A-Z]*) ?([a-z0-9]*) -> ([a-z0-9]+)')

    def parse_data(self):
        print(self.data)
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


def _parse_input(signal, register):
    if signal.isnumeric():
        return int(signal)
    else:
        return register.get(signal)


def _solve_equation(wire_1, gate, wire_2, register):
    wire_1 = _parse_input(wire_1, register)
    wire_2 = _parse_input(wire_2, register)

    func_map = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        'NOT': lambda _, x: (1 << 16) - 1 - x,
        '': lambda x, _: x
    }

    op = func_map[gate]
    result = op(wire_1, wire_2)

    if result is None:
        raise ValueError
    return result


def _assemble_wires(instructions):
    register = {}

    for wire_1, gate, wire_2, destination in instructions:
        try:
            value = _solve_equation(wire_1, gate, wire_2, register)
        except (TypeError, ValueError):
            instructions.append((wire_1, gate, wire_2, destination))
        else:
            register[destination] = value
    return register
