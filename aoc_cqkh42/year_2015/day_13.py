import itertools
import re
from collections import defaultdict

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    people = None

    def parse_data(self):
        happiness = _map_happiness(self.data)
        self.people = set(itertools.chain(*happiness))
        return happiness

    def part_a(self):
        possible_arrangements = itertools.permutations(self.people)
        return max((
            _calc_happiness(order, self.parsed_data)
            for order in possible_arrangements)
        )

    def part_b(self):
        self.people.add('me')

        possible_arrangements = itertools.permutations(self.people)
        return max((
            _calc_happiness(order, self.parsed_data)
            for order in possible_arrangements
        ))

REGEX = re.compile(r'(.*?) would.+?(-?\d+) .* (.*)\.')


def _calc_happiness(order, happy_dict):
    left = order
    right = order[1:] + order[:1]
    people = (frozenset(people) for people in zip(left, right))
    return sum(happy_dict.get(people, 0) for people in people)


def _map_happiness(data):
    data = data.replace('lose ', '-')
    matches = REGEX.findall(data)
    happiness = defaultdict(int)
    for person_a, score, person_b in matches:
        happiness[frozenset((person_a, person_b))] += int(score)
    return happiness
