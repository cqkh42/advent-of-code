from collections import defaultdict
import itertools
import re

REGEX = re.compile(r'(.*?) would.+?(-?\d+) .* (.*)\.')


def _calc_happiness(order, happy_dict):
    left = order
    right = order[1:] + order[:1]
    people = (frozenset(people) for people in zip(left, right))
    return sum(happy_dict.get(people, 0) for people in people)


def _map_happiness(data):
    data = data.replace('lose ', '-')

    matches = (re.search(REGEX, row).groups() for row in data.split('\n'))
    matches = (((person_a, person_b), score) for person_a, score, person_b in matches)

    happy_dict = defaultdict(int)
    for people, score in matches:
        happy_dict[frozenset(people)] += int(score)
    return happy_dict


def part_a(data):
    happy_dict = _map_happiness(data)
    possible_arrangements = itertools.permutations({a for b in happy_dict for a in b})
    return max((_calc_happiness(order, happy_dict) for order in possible_arrangements))


def part_b(data, **_):
    happy_dict = _map_happiness(data)
    unique_people = {a for b in happy_dict for a in b}
    unique_people.add('me')

    possible_arrangements = itertools.permutations(unique_people)
    return max((_calc_happiness(order, happy_dict) for order in possible_arrangements))
