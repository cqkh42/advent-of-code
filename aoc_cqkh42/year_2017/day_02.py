import itertools


def _row_checksum(row):
    values = [int(num) for num in row.split('\t')]
    return max(values) - min(values)


def _row_even_checksum(row):
    values = (int(num) for num in row.split('\t'))
    perms = itertools.permutations(values, 2)
    solutions = (high / low for high, low in perms if not(high % low))
    return next(solutions)


def part_a(data):
    rows = data.split('\n')
    return sum(_row_checksum(row) for row in rows)


def part_b(data, **_):
    rows = data.split('\n')
    return sum(int(_row_even_checksum(row)) for row in rows)
