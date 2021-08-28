import itertools

import parse

from aoc_cqkh42 import BaseSolution


def _route_length(route, distances):
    return sum(distances[frozenset((start, end))] for start, end in zip(route, route[1:]))


class Solution(BaseSolution):
    parser = parse.compile(r'{:w} to {:w} = {:d}')

    def parse_data(self):
        distances = {
            frozenset((site_a, site_b)): distance
            for site_a, site_b, distance in self.parser.findall(self.data)
        }
        locations = set(itertools.chain.from_iterable(distances))
        possible_routes = itertools.permutations(locations)
        return [_route_length(route, distances) for route in possible_routes]

    def part_a(self):
        return min(self.parsed_data)

    def part_b(self):
        return max(self.parsed_data)
