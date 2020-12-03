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

    matches = (REGEX.search(row).groups() for row in data.split('\n'))
    happiness = defaultdict(int)
    for person_a, score, person_b in matches:
        happiness[frozenset((person_a, person_b))] += int(score)
    return happiness


def part_a(data):
    happiness = _map_happiness(data)
    possible_arrangements = itertools.permutations(set(itertools.chain(*happiness)))
    return max((
        _calc_happiness(order, happiness)
        for order in possible_arrangements)
    )


def part_b(data, **_):
    happiness = _map_happiness(data)
    unique_people = set(itertools.chain(*happiness))
    unique_people.add('me')

    possible_arrangements = itertools.permutations(unique_people)
    return max((
        _calc_happiness(order, happiness)
        for order in possible_arrangements
    ))
