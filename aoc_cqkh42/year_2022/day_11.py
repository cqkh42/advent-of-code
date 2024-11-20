import functools
import math
import operator
from copy import deepcopy
from dataclasses import dataclass
from typing import Callable, List

import numpy as np
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    test: int
    true_: int
    false_: int
    inspected: int = 0


class Solution(BaseSolution):
    parser = parse.compile("""Monkey {monkey_num:d}:
  Starting items: {items}
  Operation: new = old {operation} {operation_num}
  Test: divisible by {test:d}
    If true: throw to monkey {true_monkey:d}
    If false: throw to monkey {false_monkey:d}""")

    def _parse(self):
        monkeys = []
        for monkey in self.parser.findall(self.input_):
            items = [int(num) for num in monkey['items'].split(', ')]
            divisor = monkey['test']
            true_ = monkey['true_monkey']
            false_ = monkey['false_monkey']
            if monkey['operation_num'] == 'old':
                if monkey['operation'] == '*':
                    operation = lambda x: x ** 2
                else:
                    operation = lambda x: x * 2
            else:
                operation_num = int(monkey['operation_num'])
                if monkey['operation'] == '*':
                    operation = functools.partial(operator.mul, operation_num)
                else:
                    operation = functools.partial(operator.add, operation_num)
            m = Monkey(items, operation, divisor, true_, false_)
            monkeys.append(m)
        return monkeys

    def generic_turn(self, container, op):
        for monkey in container:
            monkey.inspected += len(monkey.items)
            for item in monkey.items:
                value = op(monkey.operation(item))
                if value % monkey.test:
                    # we failed
                    container[monkey.false_].items.append(value)
                else:
                    container[monkey.true_].items.append(value)
            monkey.items = []
        return container

    def generic_part(self, iters, func):
        monkeys = deepcopy(self.parsed)
        for _ in range(iters):
            monkeys = self.generic_turn(monkeys, func)
        counts = sorted((monkey.inspected for monkey in monkeys),
                        reverse=True)
        return math.prod(counts[:2])

    def part_a(self):
        return self.generic_part(20, lambda x: x // 3)

    def part_b(self):
        lcm = np.lcm.reduce([monkey.test for monkey in self.parsed])
        return self.generic_part(10_000, lambda x: x % lcm)
