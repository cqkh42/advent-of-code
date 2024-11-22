import itertools

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

TRAPS = {
    "^^.":'^',
    ".^^":'^',
    "^..":'^',
    "..^": '^'
}


def calc_row(row):
    t = ["."] + row + ["."]
    triples = itertools.zip_longest(t, t[1:], t[2:], fillvalue=".")
    # triples = more_itertools.triplewise(t)
    new = [TRAPS.get(''.join(a), '.') for a in triples]
    new = new[:-2]
    return new


class Solution(BaseSolution):
    def part_a(self):
        row = list(self.input_)
        total = row.count(".")
        for step in range(39):
            row = calc_row(row)
            total += row.count(".")
        return total

    def part_b(self):
        row = list(self.input_)
        total = row.count(".")
        for step in range(399_999):
            row = calc_row(row)
            total += row.count(".")
        return total

if __name__ == "__main__":
    submit_answers(Solution, 18, 2016)
