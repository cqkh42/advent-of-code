import itertools

from aoc_cqkh42 import BaseSolution


def _increasing_combinations(item):
    combs = (
        itertools.combinations(item, length)
        for length in range(1, len(item) + 1)
    )
    yield from itertools.chain.from_iterable(combs)


class Solution(BaseSolution):
    def __init__(self, data, target=150):
        self.target = target
        super().__init__(data)

    def parse_data(self):
        containers = [int(container) for container in self.lines]
        containers = _increasing_combinations(containers)
        valid_containers = [group for group in containers if sum(group) == self.target]
        return valid_containers

    def part_a(self):
        return len(self.parsed_data)

    def part_b(self):
        sizes = [
            len(group) for group in self.parsed_data
        ]
        lowest = min(sizes)
        return sizes.count(lowest)
