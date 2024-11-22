import collections
import itertools
import re
import string
from functools import cached_property

import more_itertools
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

    @cached_property
    def num_elements(self):
        return len(self.molecule) - 1

    def get_trio(self):
        for start in range(len(self.molecule) - 1):
            for remainder in range(self.num_elements - start):
                for i in range(start + 1):
                    yield start, remainder, i

    def build_cyk(self):
        self.cyk[0] = [
            [Molecule(element)] for element in self.molecule.elements
        ]

        for start_point, remainder, i in self.get_trio():
            # print(start_point, remainder, i)
            needed_elements = [
                ''.join(more_itertools.flatten(t))
                for t in itertools.product(
                    self.cyk[i][remainder], self.cyk[start_point - i][remainder + i + 1]
                )
            ]
            # if needed_elements:
            #     print(needed_elements)
            for needed_element in needed_elements:
                missing_rules = self.rules.getall(needed_element, []).difference( self.cyk[(start_point + 1)][remainder])
                for rule in missing_rules:
                    self.cyk[start_point + 1][remainder].append(rule)
                    self.backref[start_point + 1][remainder].append(
                        (
                            (remainder, i),
                            (remainder + i + 1, start_point - i),
                            needed_element,
                        )
                    )

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
            yield "Z" + first + second

class Rules:
    letters = get_new_letter()
    def __init__(self, lines):
        a = self.input_parser(lines)
        b = [(y, x) for x, y in a]
        self.rules = MultiDict(b)

    def getall(self, key, default):
        return set(self.rules.getall(key, default))

    def _parse_line(self, line):
        left, right = line
        parts = right.elements
        if len(parts) > 2:
            letter = next(self.letters)
            new_right = parts[0] + letter
            p = Molecule(parts[1:])
            a = "".join(parts[1:])
            # assert p == Molecule(a), (p, Molecule(a))
            yield Molecule(left), Molecule(new_right)
            yield Molecule(letter), Molecule(a)
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
        # print(a)
        return a

class Molecule(str):
    reg = re.compile(r'[A-Z][a-z]?')
    def __init__(self, input_):
        if isinstance(input_, str):
            self.string = input_
            self.elements = list(self.reg.findall(input_))
        else:
            # print(input_)
            self.elements = input_
            self.string = ''.join(input_)
            # print(self.string)

    def __len__(self):
        return self._len

    @cached_property
    def _len(self):
        return len(self.elements)

    def replace(self, index, value):
        new_elements = list(self.elements)
        new_elements[index] = value
        return Molecule(''.join(new_elements))

    def __repr__(self):
        return f'Molecule("{self.string}")'
    # def __iter__(self):
    #     yield from self.elements

class Solution(BaseSolution):
    molecule = None
    rules = None

    LINE_REGEX = re.compile(r"(.+) => (.+)")

    def _parse(self):
        self.molecule = Molecule(self.lines[-1])
        self.rules = Rules(self.parsed_lines)

    def _parse_line(self, line: str):
        matches = self.LINE_REGEX.search(line)
        if matches:
            return tuple(Molecule(group) for group in matches.groups())

    def _find_simple_replacements(self, old, new):
        return {
                self.molecule.replace(index, new) for index in more_itertools.iter_index(self.molecule.elements, old)
            }

    def part_a(self):
        options = set.union(*(self._find_simple_replacements(old, new) for old, new in self.parsed_lines))
        return len(options)

    def part_b(self):
        solution = CYKRunner(self.rules, self.molecule)
        return solution.solve()


if __name__ == "__main__":
    submit_answers(Solution, 19, 2015)
