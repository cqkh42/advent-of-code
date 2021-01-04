import operator
import re

REGEX = re.compile(r'([a-z0-9]*) ?([A-Z]*) ?([a-z0-9]*) -> ([a-z0-9]+)')


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


def part_a(data):
    instructions = data.split('\n')
    instructions = [REGEX.match(inputs).groups() for inputs in instructions]
    register = _assemble_wires(instructions)
    return register['a']


def part_b(data, answer_a):
    instructions = data.split('\n')
    instructions = [REGEX.match(inputs).groups() for inputs in instructions]
    b_set_at = [output for *_, output in instructions].index('b')
    instructions[b_set_at] = (str(answer_a), '', '', 'b')
    register = _assemble_wires(instructions)
    return register['a']
