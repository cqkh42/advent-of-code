# TODO chompsky language decomposition

from aoc_cqkh42 import BaseSolution


def replace_occurence(string, old, new, occurence):
    return (
        string.replace(old, "$$$", occurence - 1)
        .replace(old, new, 1)
        .replace("$$$", old)
    )


def try_permutation(maps, element):
    visited = set()
    replaced = 0
    while element != "e":
        for new, old in maps:
            if old not in element or element.count("e"):
                continue
            element = element.replace(old, new, 1)
            if element == "e":
                return replaced + 1
            elif "e" in element:
                return None
            if element in visited:
                return None
            visited.add(element)
            replaced += 1
    return replaced


import itertools
import collections
import re
from dataclasses import dataclass, field
from functools import cached_property


@dataclass
class CYKRunner:
    molecule: str
    rules: collections.defaultdict
    revrules: collections.defaultdict
    calibrate: set
    cyk: collections.defaultdict = field(
        default_factory=lambda: collections.defaultdict(
            lambda: collections.defaultdict(list)))
    backref: collections.defaultdict = field(
        default_factory=lambda: collections.defaultdict(
            lambda: collections.defaultdict(list)))
    counter: int = field(default=0)

    @cached_property
    def letters(self):
        return len(self.molecule) - 1

    def run(self):
        for index, element in enumerate(self.molecule):
            self.cyk[0][index] = [element]
        for y in range(1, self.letters + 1):
            for x in range(self.letters - y + 1):
                for i in range(y):
                    need = [t[0] + t[1] for t in
                            itertools.product(self.cyk[i][x],
                                              self.cyk[y - i - 1][x + i + 1])]
                    for n in need:
                        for blah in self.revrules.get("".join(n), []):
                            if blah not in self.cyk[y][x]:
                                self.cyk[y][x].append(blah)
                                self.backref[y][x].append(
                                    ((x, i), (x + i + 1, y - i - 1), n))

    def recur(self, x,
              y):  # TODO: IS THIS WRONG IF THE FIRST EXPANSION FOUND IS NONOPTIMAL? (probably not because CNF)
        if y == 0:
            return
        l, r, n = self.backref[y][x][0]
        self.counter += not self.cyk[y][x][0].startswith('Z')
        self.recur(*l)
        self.recur(*r)


def run(input, molecule):
    calibrate = set()
    rules = collections.defaultdict(list)
    revrules = collections.defaultdict(list)

    pattern = r"(.+) => (.+)"
    for src, repl in re.findall(pattern, input):
        rules[src] += [repl]
        revrules[repl] += [src]

    for src, repl in re.findall(pattern, input):
        for start in re.finditer(src, ''.join(molecule)):
            start = start.start()
            calibrate.add(''.join(molecule[:start]) + repl + ''.join(
                molecule[start + len(src):]))

    solution = CYKRunner(molecule, rules, revrules, calibrate)
    solution.run()
    solution.recur(0, solution.letters)
    return solution.counter


class Solution(BaseSolution):
    element = None
    maps = None

    def parse_data(self):
        *maps, _, element = self.lines
        maps = [item.split(" => ") for item in maps]
        self.element = element
        self.maps = maps
        return maps, element

    def part_a(self):
        new_strings = set()
        for old, new in self.maps:
            count = self.element.count(old)
            for occurence in range(1, count + 1):
                new_string = replace_occurence(self.element, old, new,
                                               occurence)
                new_strings.add(new_string)
        return len(new_strings)

    def part_b(self):
        return run(self.maps, self.element)
# TODO: CAN JUST KEEP A COUNTER IN RECUR
