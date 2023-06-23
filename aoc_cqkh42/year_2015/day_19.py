import collections
import itertools
import re
from functools import cached_property

from multidict import MultiDict

from aoc_cqkh42 import BaseSolution
from .day_19_help import input_


class NewCYKRunner:
    def __init__(self, rules, molecule):
        self.rules = rules

        self.molecule = molecule
        self.cyk = collections.defaultdict(
            lambda: collections.defaultdict(list))
        self.backref = collections.defaultdict(
            lambda: collections.defaultdict(list))
        self.counter = 0

    @cached_property
    def elements(self):
        return sum(char.isupper() for char in self.molecule) - 1

    def run(self):
        for index, element in enumerate(
                re.findall(r'[A-Z][a-z]?', self.molecule)):
            self.cyk[0][index] = [element]

        for y in range(1, self.elements + 1):
            for x in range(self.elements - y + 1):
                for i in range(y):
                    need = [t[0] + t[1] for t in
                            itertools.product(self.cyk[i][x],
                                              self.cyk[y - i - 1][x + i + 1])]
                    for n in need:
                        for blah in self.rules.getall("".join(n), []):
                            if blah not in self.cyk[y][x]:
                                self.cyk[y][x].append(blah)
                                self.backref[y][x].append(
                                    ((x, i), (x + i + 1, y - i - 1), n))

    def recur(self, x, y):
        if y == 0:
            return
        l, r, n = self.backref[y][x][0]
        self.counter += not self.cyk[y][x][0].startswith('Z')
        self.recur(*l)
        self.recur(*r)


class Solution(BaseSolution):
    new_maps = input_
    molecule = None
    rules = None

    def parse_data(self):
        self.molecule = self.lines[-1]
        self.rules = MultiDict(
            ((v, k) for k, v in re.findall(r"(.+) => (.+)", input_)))

    def part_a(self):
        new_strings = set()
        for old, new in re.findall(r"(.+) => (.+)", self.data):
            replacements = {
                self.molecule[:i.start()] + new + self.molecule[i.end():] for i
                in re.finditer(old, self.molecule)}

            new_strings.update(replacements)
        return len(new_strings)

    def part_b(self):
        solution = NewCYKRunner(self.rules, self.molecule)
        solution.run()
        solution.recur(0, solution.elements)
        return solution.counter
