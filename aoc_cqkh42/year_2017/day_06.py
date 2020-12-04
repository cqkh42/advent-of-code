import itertools


def _distribute(banks):
    being_distributed = banks.index(max(banks))
    to_distribute = banks[being_distributed]
    banks[being_distributed] = 0
    for block in range(to_distribute):
        index = (block + being_distributed + 1) % len(banks)
        banks[index] += 1
    return banks


def part_a(data):
    seen = set()
    banks = [int(bank) for bank in data.split('\t')]
    seen.add(tuple(banks))

    for dist in itertools.count(1):
        banks = _distribute(banks)
        if tuple(banks) in seen:
            return dist
        seen.add(tuple(banks))
    return False


def part_b(data, **_):
    banks = [int(bank) for bank in data.split('\t')]
    seen = {tuple(banks): 1}

    for dist in itertools.count(1):
        banks = _distribute(banks)
        if tuple(banks) in seen:
            return dist - seen[tuple(banks)]
        seen[tuple(banks)] = dist
