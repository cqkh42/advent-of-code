import functools

import numpy as np

from aoc_cqkh42.helpers.base_solution import BaseSolution


@functools.cache
def tri_cost_of_point(numbers, point):
    total = 0
    for number in numbers:
        diff = abs(number - point)
        cost = sum(range(diff + 1))
        total += cost
    return total


class Solution(BaseSolution):
    def parse_data(self):
        return tuple(int(num) for num in self.data.split(','))

    def part_a(self):
        median = np.median(self.parsed_data).astype(int)
        fuel_cost = [abs(num - median) for num in self.parsed_data]
        return sum(fuel_cost)

    def part_b(self):
        start = min(self.parsed_data)
        end = max(self.parsed_data) + 1
        for point in range(start, end):
            this_cost = tri_cost_of_point(self.parsed_data, point)
            if tri_cost_of_point(self.parsed_data, point+1) > this_cost:
                return this_cost
