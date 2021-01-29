import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        containers = [int(container) for container in self.data.split('\n')]
        containers = list(_increasing_combinations(containers))
        return containers

    def part_a(self):
        valid_containers = (
            sum(group) == 150
            for group in self.parsed_data
        )
        return sum(valid_containers)

    def part_b(self):
        valid_containers = [
            len(group) for group in self.parsed_data
            if sum(group) == 150
        ]
        lowest = min(valid_containers)
        return valid_containers.count(lowest)


def _increasing_combinations(item):
    combs = (
        itertools.combinations(item, length)
        for length in range(1, len(item) + 1)
    )
    return itertools.chain.from_iterable(combs)
