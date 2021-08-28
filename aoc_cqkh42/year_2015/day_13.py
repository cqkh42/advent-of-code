import itertools
from collections import defaultdict

import parse

from aoc_cqkh42 import BaseSolution


PARSER = parse.compile(
    r'{a:w} would {change:d} happiness units by sitting next to {b:w}.'
)


def _map_happiness(data):
    data = data.replace('lose ', '-').replace('gain ', '')
    matches = PARSER.findall(data)
    score = defaultdict(int)
    for match in matches:
        score[frozenset((match['a'], match['b']))] += int(match['change'])
    return score


class Solution(BaseSolution):
    people = None

    def parse_data(self):
        happiness = _map_happiness(self.data)
        self.people = set(itertools.chain(*happiness))
        return happiness

    def _calc_happiness(self, order):
        left = order
        right = order[1:] + order[:1]
        people = (frozenset(people) for people in zip(left, right))
        return sum(self.parsed_data[people] for people in people)

    def part_a(self):
        possible_arrangements = itertools.permutations(self.people)
        return max((
            self._calc_happiness(order)
            for order in possible_arrangements)
        )

    def part_b(self):
        self.people.add('me')
        possible_arrangements = itertools.permutations(self.people)
        return max((
            self._calc_happiness(order)
            for order in possible_arrangements
        ))
