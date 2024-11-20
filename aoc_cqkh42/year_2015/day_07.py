#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/7
"""
__all__ = ["Solution"]
import operator
import re
from collections import UserDict
from dataclasses import dataclass

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

FUNC_MAP = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": lambda x: (1 << 16) - 1 - x,
}


@dataclass
class Register:
    def __init__(self, lines):
        self.register = {}
        for line in lines:
            self.add_line(line)

    def add_line(self, line):
        match line.split():
            case [wire_1, op, wire_2, "->", destination]:
                self.register[destination] = (op, (wire_1, wire_2))
            case [op, wire, "->", destination]:
                self.register[destination] = (op, (wire,))
            case [wire, "->", destination]:
                self.register[destination] = wire

    def resolve(self, key):
        match self[key]:
            case str(value):
                self[key] = self.resolve(value)
            case (op, inputs):
                inputs = (self.resolve(input_) for input_ in inputs)
                value = FUNC_MAP[op](*inputs)
                self[key] = value
        return self[key]

    def __getitem__(self, key):
        if isinstance(key, int) or key.isnumeric():
            return int(key)
        return self.register.get(key, key)

    def __setitem__(self, key, value):
        self.register[key] = value


class Solution(BaseSolution):
    """Solutions for day 7 of 2015's Advent of Code."""

    answer_a = None

    def part_a(self):
        register = Register(self.lines)
        self.answer_a = register.resolve("a")
        return self.answer_a

    def part_b(self):
        register = Register(self.lines)
        register["b"] = self.answer_a
        return register.resolve("a")


if __name__ == "__main__":
    submit_answers(Solution, 7, 2015)
