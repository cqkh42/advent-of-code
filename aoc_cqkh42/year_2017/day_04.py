from typing import Self

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def sort_words(phrase):
    return [sorted(word) for word in phrase]


class Solution(BaseSolution):
    def _process_data(self: Self) -> list[list[str]]:
        return [line.split() for line in self.lines]

    def part_a(self):
        return sum(more_itertools.all_unique(line) for line in self.processed)

    def part_b(self):
        sorted_ = (sort_words(phrase) for phrase in self.processed)
        return sum(more_itertools.all_unique(line) for line in sorted_)


if __name__ == "__main__":
    submit_answers(Solution, 4, 2017)
