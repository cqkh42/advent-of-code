from collections import Counter
from string import ascii_letters

import more_itertools

from aoc_cqkh42 import BaseSolution


def count_total(counts):
    return sum(
        (ascii_letters.index(letter) + 1) * count
        for letter, count in counts.items()
    )


class Solution(BaseSolution):
    def part_a(self):
        lines = (more_itertools.divide(2, line) for line in self.lines)
        totals = Counter(
            more_itertools.one(set(left).intersection(right))
            for left, right in lines
        )
        return count_total(totals)

    def part_b(self):
        intersections = Counter(
            more_itertools.one(set(first).intersection(*others))
            for first, *others in more_itertools.chunked(self.lines, 3)
        )
        return count_total(intersections)
