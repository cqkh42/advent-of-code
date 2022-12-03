from aoc_cqkh42 import BaseSolution

from collections import Counter
from string import ascii_letters


def make_chunks(lst, n):
    #todo make this a helper
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Solution(BaseSolution):
    def part_a(self):
        totals = Counter(
            max(set(line[:len(line)//2]).intersection(line[len(line)//2:]))
            for line in self.lines
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
