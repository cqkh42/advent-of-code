import math
import re
from collections import defaultdict
from dataclasses import dataclass

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Replacement:
    element: str
    quantity: int
    replacements: dict


def next_element(f):
    for element in f:
        if f[element] > 0 and element != 'ORE':
            return element


def _count_iterations(needs, gives):
    return math.ceil(needs / gives)


def extract_conversions(data):
    first = [re.search(r'(.*?) => (\d+) (\w+)', row).groups() for row in
             data.split('\n')]
    finals = {}
    for repls, quantity, element in first:
        r = re.finditer(r'(\d+) (\w+)', repls)
        r = (i.groups() for i in r)
        r = {b: int(a) for a, b in r}
        o = Replacement(element, int(quantity), r)
        finals[element] = o
    return finals


def ore_needed(conversions, fuel_needed=1):
    f = {k: v*fuel_needed for k, v in conversions['FUEL'].replacements.items()}
    FUEL = defaultdict(int, f)
    element = next_element(FUEL)
    while element:
        repl = conversions[element]
        runs_n_times = _count_iterations(FUEL[element], repl.quantity)
        makes = runs_n_times * repl.quantity

        FUEL[element] -= makes
        for e in repl.replacements:
            FUEL[e] += repl.replacements[e] * runs_n_times
        element = next_element(FUEL)
    return FUEL['ORE']


def fuel_with_ore(reactions, ore):
    lower = 0
    n = 0

    result = 0
    while result <= ore:
        result = ore_needed(reactions, 10 ** n)
        upper = 10 ** n
        lower = 10 ** (n - 1)
        if result >= ore:
            break
        n += 1
    while True:
        half = int((upper + lower) / 2)
        result = ore_needed(reactions, half)
        if result > ore:
            upper = half
        elif result < ore:
            lower = half
            if ore_needed(reactions, half + 1) > ore:
                return half


class Solution(BaseSolution):
    def _parse(self):
        return extract_conversions(self.input_)

    def part_a(self):
        return ore_needed(self.parsed, 1)

    def part_b(self):
        return fuel_with_ore(self.parsed, 1e12)
