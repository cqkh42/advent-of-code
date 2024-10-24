from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

import more_itertools
import itertools

def is_caught(time, size):
    return not time % (2*size - 2)

class Solution(BaseSolution):
    def _process_data(self: Self) -> list[tuple[int, int]]:
        lines = [line.split(': ') for line in self.lines]
        return [(int(l), int(r)) for l, r in lines]


    def part_a(self):
        return sum(l*r for l, r in self.processed if is_caught(l, r))

    def part_b(self):
        for delay in itertools.count():
            locations = ((l+delay, r) for l, r in self.processed)
            if any(is_caught (l, r) for l,r in locations):
                continue
            else:
                return delay
        return None


if __name__ == "__main__":
    submit_answers(Solution, 13, 2017)