import itertools


def _build_route(route):
    steps = [[order[0]] * int(order[1:]) for order in route.split(',')]
    mapping = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    steps = [mapping[step] for step in itertools.chain.from_iterable(steps)]
    x, y = zip(*steps)
    x = itertools.accumulate(x)
    y = itertools.accumulate(y)
    visited = ((x, y) for x, y in zip(x, y))
    return visited


def _sum_indices(value, lists):
    return sum(list_.index(value) for list_ in lists)


def part_a(data):
    routes = (set(_build_route(route)) for route in data.split('\n'))
    intersections = set.intersection(*routes)
    distances = (abs(x) + abs(y) for x, y in intersections)
    return min(distances)


def part_b(data, **_):
    routes = [list(_build_route(route)) for route in data.split('\n')]
    set_routes = (set(route) for route in routes)
    intersections = set.intersection(*set_routes)
    distances = (
        _sum_indices(intersection, routes) + len(routes)
        for intersection in intersections
    )
    return min(distances)
