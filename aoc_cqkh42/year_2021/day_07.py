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
    def _process_data(self):
        return tuple(int(num) for num in self.input_.split(','))

    def part_a(self):
        median = np.median(self.processed).astype(int)
        fuel_cost = [abs(num - median) for num in self.processed]
        return sum(fuel_cost)

    def part_b(self):
        start = min(self.processed)
        end = max(self.processed) + 1
        for point in range(start, end):
            this_cost = tri_cost_of_point(self.processed, point)
            if tri_cost_of_point(self.processed, point + 1) > this_cost:
                return this_cost
