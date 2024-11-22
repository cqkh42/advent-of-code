import collections
import itertools
import re
import string
from collections import defaultdict
from functools import cached_property

import more_itertools
from more_itertools.recipes import iter_index
from multidict import MultiDict

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class CYKRunner:
    def __init__(self, rules, molecule):
        self.rules = rules

        self.molecule = molecule
        self.cyk: dict[int, list] = collections.defaultdict(
            lambda: [[] for _ in range(1000)]
        )
        self.backref = collections.defaultdict(lambda: [[] for _ in range(1000)])
        self.counter = 0
        self.build_cyk()

    def get_trio(self):
        for start in range(len(self.molecule) - 1):
            for remainder in range(len(self.molecule) - start - 1):
                for i in range(start + 1):
                    yield start, remainder, i

    def build_cyk(self):
        self.cyk[0] = [
            [Molecule(element)] for element in self.molecule.elements
        ]

        for start, remainder, i in self.get_trio():
            needed_elements = [
                Molecule(''.join(more_itertools.flatten(t)))
                for t in itertools.product(
                    self.cyk[i][remainder], self.cyk[start - i][remainder + i + 1]
                )
            ]
            for needed_element in needed_elements:
                missing_rules = self.rules[needed_element].difference( self.cyk[(start + 1)][remainder])
                self.cyk[start + 1][remainder].extend(missing_rules)
                a = ((remainder, i), (remainder + i + 1, start - i), needed_element)
                self.backref[start + 1][remainder].extend([a]* len(missing_rules))

    def solve(self):
        self._solve(0, len(self.molecule)-1)
        return self.counter

    def _solve(self, x, y):
        if not y:
            return
        l, r, n = self.backref[y][x][0]
        self.counter += not self.cyk[y][x][0].startswith("Z")
        self._solve(*l)
        self._solve(*r)


def get_new_letter():
    for first in string.ascii_lowercase:
        for second in string.ascii_lowercase:
            yield Molecule("Z" + first + second)

class RuleBuilder:
    letters = get_new_letter()

    def build(self, lines):
        a = self.input_parser(lines)
        b = [(y, x) for x, y in a]
        rules = defaultdict(set)
        for y, x in b:
            rules[y].add(x)
        return rules

    def _parse_line(self, line):
        left, right = line
        parts = right.elements
        if len(parts) > 2:
            letter = next(self.letters)
            new_right = parts[0] + letter
            p = Molecule(parts[1:])
            yield Molecule(left), Molecule(new_right)
            yield from self._parse_line((Molecule(letter), p))
        else:
            yield Molecule(left), Molecule(right)

    def __repr__(self):
        return self.rules

    def __str__(self):
        return self.rules.__str__()

    def parse_line(self, line):
        a = set(self._parse_line(line))
        b = {i for i in a if len(i[1]) <= 2}
        return b

    def input_parser(self, lines):
        lines = (self.parse_line(line) for line in lines)
        a = list(set.union(*lines))
        return a

class Molecule(str):
    reg = re.compile(r'[A-Z][a-z]?')
    def __init__(self, input_):
        if isinstance(input_, Molecule):
            self.string = input_.string
            self.elements = input_.elements
        if isinstance(input_, str):
            self.string = input_
            self.elements = list(self.reg.findall(input_))
        else:
            self.elements = input_
            self.string = ''.join(input_)

    def __len__(self):
        return self._len

    def __eq__(self, other):
        if isinstance(other, Molecule):
            return self.elements == other.elements
        elif isinstance(other, str):
            return self == Molecule(other)
        else:
            raise NotImplementedError(f'Cannot compare Molecule and {type(other)}')

    def __hash__(self):
        return hash(tuple(self.elements))

    @cached_property
    def _len(self):
        return len(self.elements)

    def replace(self, index, value):
        a = self.elements[:index]
        b = self.elements[index+1:]
        new = [*a, *value.elements, *b]
        return Molecule(new)

    def __repr__(self):
        return f'Molecule("{self.string}")'


class Solution(BaseSolution):
    molecule = None
    rules = None

    LINE_REGEX = re.compile(r"(.+) => (.+)")

    def _parse(self):
        self.molecule = Molecule(self.lines[-1])
        self.rules = RuleBuilder().build(self.parsed_lines)

    def _parse_line(self, line: str):
        matches = self.LINE_REGEX.search(line)
        if matches:
            return tuple(Molecule(group) for group in matches.groups())

    def _find_simple_replacements(self, old, new):
        return {
            self.molecule.replace(index, new)
            for index in iter_index(self.molecule.elements, old)
        }

    def part_a(self):
        options = set.union(*(self._find_simple_replacements(old, new) for old, new in self.parsed_lines))
        return len(options)

    def part_b(self):
        solution = CYKRunner(self.rules, self.molecule)
        return solution.solve()


if __name__ == "__main__":
    submit_answers(Solution, 19, 2015)
