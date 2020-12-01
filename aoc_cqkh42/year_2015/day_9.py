import itertools
import re


def _route_length(route, distances):
    return sum(distances[(start, end)] for start, end in zip(route, route[1:]))


def _find_distances(routes):
    distances = {}
    regex = re.compile(r'(.*?) to (.*?) = (\d+)')
    for route in routes:
        site_a, site_b, distance = re.match(regex, route).groups()
        distances[(site_a, site_b)] = int(distance)
        distances[(site_b, site_a)] = int(distance)
    locations = {site for pair in distances for site in pair}
    possible_routes = itertools.permutations(locations)
    return (_route_length(route, distances) for route in possible_routes)


def part_a(data):
    return min(_find_distances(data.split('\n')))


def part_b(data, **_):
    return max(_find_distances(data.split('\n')))
