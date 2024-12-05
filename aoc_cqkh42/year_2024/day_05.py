from functools import cached_property
from random import sample
from typing import Self, Any

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Update:
    def __init__(self, update, rules):
        self.update = update
        self.rules = rules

    @cached_property
    def is_valid(self):
        return all(self.index(left) < self.index(right) for left, right in
            self.rules)

    @cached_property
    def median(self):
        return self.update[(len(self) - 1) // 2]

    def __len__(self):
        return len(self.update)

    def index(self, value):
        return self.update.index(value)

    def broken_rules(self):
        return [(left, right) for left, right in
            self.rules if self.index(left) >= self.index(right)]

    def fix_rules(self):
        new_update = self.update.copy()
        for left, right in self.broken_rules():
            new_update.remove(left)
            new_update.insert(new_update.index(right), left)
        return Update(new_update, sample(self.rules, k=len(self.rules)))

    def __repr__(self):
        return f"Update({self.update})"


class Solution(BaseSolution):
    PARSER = parse.compile('{:d}')
    rules = None
    updates = None

    def _parse(self: Self) -> Any:
        rules, updates = self.input_.split('\n\n')
        rules = [line.split('|') for line in rules.split('\n')]
        self.rules = [(int(left), int(right)) for left, right in rules]

        raw_updates = [[num[0] for num in self.PARSER.findall(update)] for update in updates.split('\n')]
        updates = []
        for update in raw_updates:
            valid_rules = [rule for rule in self.rules if
                           set(rule).issubset(update)]
            updates.append(Update(update, valid_rules))
        self.updates = updates

    def part_a(self):
        return sum(update.median for update in self.updates if update.is_valid)

    def part_b(self):
        solved = []
        invalid_updates = [update for update in self.updates if not update.is_valid]
        while invalid_updates:
            update = invalid_updates.pop()
            new_update = update.fix_rules()
            if new_update.is_valid:
                solved.append(new_update)
            else:
                invalid_updates.append(new_update)
        return sum(update.median for update in solved if update.is_valid)


if __name__ == "__main__":
    submit_answers(Solution,5, 2024)
