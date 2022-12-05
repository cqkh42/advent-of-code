from aoc_cqkh42 import BaseSolution
#TODO how many places can we use more_itertools
from collections import Counter
from string import ascii_letters

from aoc_cqkh42.helpers.helpers import make_chunks

import more_itertools

class Solution(BaseSolution):
    def part_a(self):
        lines = (more_itertools.divide(2, line) for line in self.lines)
        totals = Counter(
            max(set(a).intersection(b))
            for a,b in lines
        )
        return sum(
            (ascii_letters.index(letter) + 1) * count
            for letter, count in totals.items()
        )

    def part_b(self):
        intersections = Counter(
            max(set(a).intersection(b, c))
            for a, b, c in make_chunks(self.lines, 3)
        )
        return sum(
            (ascii_letters.index(letter) + 1) * count
            for letter, count in intersections.items()
        )
