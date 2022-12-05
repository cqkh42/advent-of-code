from collections import Counter
import functools

from aoc_cqkh42 import BaseSolution

import more_itertools
@functools.cache
def valid(numbers, target):
    containers = more_itertools.powerset(numbers)
    valid_containers = [group for group in containers if
                        sum(group) == target]
    return valid_containers


class Solution(BaseSolution):
    def part_a(self, target=150):
        return len(valid(self.numbers, target))

    def part_b(self, target=150):
        sizes = Counter(
            len(group) for group in valid(self.numbers, target)
        )
        return sizes[min(sizes)]
