from functools import lru_cache


def _sort_adapters(adapters):
    adapters = [0, *sorted(adapters), max(adapters) + 3]
    return adapters


def part_a(data):
    adapters = [int(num) for num in data.split('\n')]
    adapters = _sort_adapters(adapters)
    differences = [b-a for a, b in zip(adapters, adapters[1:])]
    return differences.count(1) * differences.count(3)


def _chain_adapters(adapters):
    chain = [0] * (max(adapters) + 1)
    for num in adapters:
        chain[num] = tuple(
            next_num for next_num in adapters
            if 1 <= next_num - num <= 3
        )
    return tuple(chain)


@lru_cache(1000)
def _num_routes(num, k):
    if not k[num]:
        return 1
    else:
        return sum(_num_routes(x, k) for x in k[num])


def part_b(data, **_):
    adapters = [int(num) for num in data.split('\n')]
    adapters = _sort_adapters(adapters)
    chain = _chain_adapters(adapters)
    return _num_routes(0, chain)
