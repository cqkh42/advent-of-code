from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        return sum(_fuel_needed(module) for module in self.numbers)

    def part_b(self):
        return sum(_total_fuel_needed(module) for module in self.numbers)


def _fuel_needed(module):
    return max(module // 3 - 2, 0)


def _total_fuel_needed(module):
    fuel = _fuel_needed(module)
    if not fuel:
        return fuel
    return fuel + _total_fuel_needed(fuel)
