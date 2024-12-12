from collections import UserDict
from functools import cached_property
from operator import eq, gt, lt

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile("{:w}: {:d}")


class Sue(UserDict):
    def __init__(self, data):
        sue = PARSER.findall(data)
        super().__init__(sue)

    auntie = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    @cached_property
    def intersection(self):
        return set(self).intersection(self.auntie)

    def is_good(self):
        return all(self[item] == self.auntie[item] for item in self.intersection)

    def is_real_sue(self):
        ops = {
            'cats': gt,
            'trees': gt,
            'pomeranians': lt,
            'goldfish': lt
        }
        return all(ops.get(key, eq)(self[key], self.auntie[key]) for key in self.intersection)


class Solution(BaseSolution):
    def part_a(self):
        sue_is_good = [sue.is_good() for sue in self.lines_as(Sue)]
        return sue_is_good.index(True) + 1

    def part_b(self):
        is_good_sue = [sue.is_real_sue() for sue in self.lines_as(Sue)]
        return is_good_sue.index(True) + 1


if __name__ == "__main__":
    submit_answers(Solution, 16, 2015)
