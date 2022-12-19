from aoc_cqkh42 import BaseSolution

from dataclasses import dataclass, field
from copy import deepcopy
from typing import List, Callable
import operator
import functools
import parse
import math


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

    def parse_data(self):
        monkeys = []
        for monkey in self.parser.findall(self.data):
            items = [int(num) for num in monkey['items'].split(', ')]
            divisor = monkey['test']
            true_ = monkey['true_monkey']
            false_ = monkey['false_monkey']
            if monkey['operation_num'] == 'old':
                if monkey['operation'] == '*':
                    operation = lambda x: x ** 2
                else:
                    operation = lambda x: x * 2
                m = Monkey(items, operation, divisor, true_, false_)
            else:
                operation_num = int(monkey['operation_num'])
                if monkey['operation'] == '*':
                    operation = functools.partial(operator.mul, operation_num)
                else:
                    operation = functools.partial(operator.add, operation_num)
                m = Monkey(items, operation, divisor, true_, false_)
            monkeys.append(m)
        return monkeys

    def turn(self):
        for monkey in self.parsed_data:
            for item in monkey.items:
                monkey.inspected += 1
                # print(monkey.operation)
                value = monkey.operation(item) // 3
                if value % monkey.test:
                    # we failed
                    self.parsed_data[monkey.false_].items.append(value)
                else:
                    self.parsed_data[monkey.true_].items.append(value)
            monkey.items = []


    def turn_b(self):
        return
        for monkey in self.parsed_data:
            for item in monkey.items:
                monkey.inspected += 1
                # print(monkey.operation)
                value = monkey.operation(item) // 3
                if value % monkey.test:
                    # we failed
                    self.parsed_data[monkey.false_].items.append(value)
                else:
                    self.parsed_data[monkey.true_].items.append(value)
            monkey.items = []


    def part_a(self):
        for _ in range(20):
            self.turn()
        counts = sorted((monkey.inspected for monkey in self.parsed_data), reverse=True)
        return math.prod(counts[:2])



    def part_b(self):
        return
        for _ in range(10_000):
            self.turn()
        counts = sorted((monkey.inspected for monkey in self.parsed_data), reverse=True)
        return math.prod(counts[:2])
