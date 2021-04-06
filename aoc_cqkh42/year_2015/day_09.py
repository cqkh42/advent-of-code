# TODO use parse here

import itertools
import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    regex = re.compile(r'(.*?) to (.*?) = (\d+)')

    def parse_data(self):
        distances = {}
        for site_a, site_b, distance in self.regex.findall(self.data):
            distances[(site_a, site_b)] = int(distance)
            distances[(site_b, site_a)] = int(distance)
        locations = {site for pair in distances for site in pair}
        possible_routes = itertools.permutations(locations)
        return [_route_length(route, distances) for route in possible_routes]

    def part_a(self):
        return min(self.parsed_data)

    def part_b(self):
        return max(self.parsed_data)


def _route_length(route, distances):
    return sum(distances[(start, end)] for start, end in zip(route, route[1:]))
