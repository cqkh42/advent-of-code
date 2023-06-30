import functools
from collections import Counter
from typing import Self

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution


@functools.cache
def valid(numbers, target):
    containers = more_itertools.powerset(numbers)
    valid_containers = [group for group in containers if sum(group) == target]
    return valid_containers


class Solution(BaseSolution):
    def part_a(self, target=150):
        return len(valid(self.numbers, target))

    def part_b(self, target=150):
        sizes = Counter(len(group) for group in valid(self.numbers, target))
        return sizes[min(sizes)]

    def _parse_data(self: Self) -> str:
        return self.data
