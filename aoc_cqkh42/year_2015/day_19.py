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
        self.run()

    @cached_property
    def num_elements(self):
        return sum(char.isupper() for char in self.molecule) - 1

    def get_trio(self):
        for start in range(self.num_elements):
            for remainder in range(self.num_elements - start):
                for i in range(start + 1):
                    yield start, remainder, i

    def run(self):
        self.cyk[0] = [
            [element] for element in re.findall(r"[A-Z][a-z]?", self.molecule)
        ]

        for start_point, remainder, i in self.get_trio():
            needed_elements = [
                more_itertools.flatten(t)
                for t in itertools.product(
                    self.cyk[i][remainder], self.cyk[start_point - i][remainder + i + 1]
                )
            ]
            for needed_element in needed_elements:
                missing_rules = (
                    rule
                    for rule in self.rules.getall("".join(needed_element), [])
                    if rule not in self.cyk[(start_point + 1)][remainder]
                )
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
        self._solve(0, self.num_elements)
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


def input_parser(lines):
    a = [right for left, right in lines]
    a = [sum(char.isupper() for char in right) for right in a]
    if max(a) == 2:
        return lines
    else:
        letters = get_new_letter()
        new = []
        for left, right in lines:
            parts = re.findall("[A-Z][a-z]?", right)

            if len(parts) > 2:
                letter = next(letters)
                new_right = parts[0] + letter
                new.append((left, new_right))
                new.append((letter, "".join(parts[1:])))
            else:
                new.append((left, right))
        return input_parser(new)


class Solution(BaseSolution):
    molecule = None
    rules = None

    def _parse(self):
        self.molecule = self.lines[-1]
        a = input_parser(re.findall(r"(.+) => (.+)", self.input_))
        self.rules = MultiDict(((v, k) for k, v in a))

    def part_a(self):
        new_strings = set()
        for old, new in re.findall(r"(.+) => (.+)", self.input_):
            replacements = {
                self.molecule[: i.start()] + new + self.molecule[i.end() :]
                for i in re.finditer(old, self.molecule)
            }
            new_strings.update(replacements)
        return len(new_strings)

    def part_b(self):
        solution = CYKRunner(self.rules, self.molecule)
        return solution.solve()


if __name__ == "__main__":
    submit_answers(Solution, 19, 2015)
