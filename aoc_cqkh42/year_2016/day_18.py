import itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution

TRAPS = {"^^.", ".^^", "^..", "..^"}


def calc_row(row):
    t = "." + row + "."
    triples = itertools.zip_longest(t, t[1:], t[2:], fillvalue=".")
    new = ["^" if "".join(a) in TRAPS else "." for a in triples]
    new = new[:-2]
    return "".join(new)


class Solution(BaseSolution):
    def part_a(self):
        row = self.input_
        total = row.count(".")
        for step in range(39):
            row = calc_row(row)
            total += row.count(".")
        return total

    def part_b(self):
        row = self.input_
        total = row.count(".")
        for step in range(399_999):
            row = calc_row(row)
            total += row.count(".")
        return total
