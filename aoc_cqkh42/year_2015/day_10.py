from functools import lru_cache
import itertools


@lru_cache()
def _look_and_see(sequence):
    g = itertools.groupby(sequence)
    d = (f'{len(list(b))}{a}' for a, b in g)
    return ''.join(d)


def part_a(data, iters=40):
    for _ in range(iters):
        data = _look_and_see(data)
    return len(data)


def part_b(data, **_):
    for _ in range(50):
        data = _look_and_see(data)
    return len(data)
