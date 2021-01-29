import re

import parse

from aoc_cqkh42 import BaseSolution

p = parse.compile('{:w}: {:d}, {:w}: {:d}, {:w}: {:d}')
class Solution(BaseSolution):
    def parse_data(self):
        sue_list = REGEX.findall(self.data)
        sue_list = [
            dict(zip(bits[::2], [int(num) for num in bits[1::2]]))
            for bits in sue_list
        ]
        return sue_list

    def part_a(self):
        sue_is_good = [all(sue[key] == AUNTIE[key] for key in sue) for sue in
                       self.parsed_data]
        return sue_is_good.index(True) + 1

    def part_b(self):
        is_good_sue = [_good_sue(sue) for sue in self.parsed_data]
        return is_good_sue.index(True) + 1

REGEX = re.compile(r'Sue \d+: (.*?): (\d+), (.*?): (\d+), (.*?): (\d+)')

# noinspection SpellCheckingInspection
AUNTIE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


# noinspection SpellCheckingInspection
def _good_sue(sue):
    equals = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']
    equals = all(sue[attr] == AUNTIE[attr] for attr in equals if attr in sue)

    gt = ['cats', 'trees']
    gt = all(sue[attr] > AUNTIE[attr] for attr in gt if attr in sue)

    lt = ['pomeranians', 'goldfish']
    lt = all(sue[attr] < AUNTIE[attr] for attr in lt if attr in sue)
    return equals and gt and lt
