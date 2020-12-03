import itertools


def _trace_path(steps):
    mapping_dict = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    x, y = zip(*(mapping_dict[step] for step in steps))
    x = itertools.accumulate(x)
    y = itertools.accumulate(y)
    visited = set(zip(x, y))
    visited.add((0, 0))
    return visited


def part_a(data):
    return len(_trace_path(data))


def part_b(data, **_):
    santa = _trace_path(data[::2])
    robo = _trace_path(data[1::2])
    visited = {*santa, *robo}
    return len(visited)
